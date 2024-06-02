from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.data_transformation import DataTransformation
from TextSummarizer.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_transformation_config()
        data_trasformation = DataTransformation(config=data_transformation_config)
        data_trasformation.convert()

