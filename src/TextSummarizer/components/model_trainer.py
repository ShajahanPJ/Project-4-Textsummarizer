from transformers import Trainer, TrainingArguments, DataCollatorForSeq2Seq, AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_from_disk
from TextSummarizer.entity import ModelTrainerConfig
import os
import torch

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Load the tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt) 
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        
        # Create a data collator (for batches)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)
        
        # Load data
        dataset_samsum_pt = load_from_disk(self.config.data_path)
        
        # Define training arguments
        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=1,
            warmup_steps=500,
            per_device_train_batch_size=4,
            per_device_eval_batch_size=4,
            weight_decay=0.01,
            logging_steps=10,
            eval_strategy='steps',
            eval_steps=500,
            save_steps=1e6,
            gradient_accumulation_steps=16,
            fp16=True
        )
        
        # Initialize the Trainer
        trainer = Trainer(
            model=model_pegasus,
            args=trainer_args,
            tokenizer=tokenizer,
            data_collator=seq2seq_data_collator,
            train_dataset=dataset_samsum_pt["train"],
            eval_dataset=dataset_samsum_pt["validation"]
        )
        
        trainer.train()

        # Save model
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))
        # Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))

