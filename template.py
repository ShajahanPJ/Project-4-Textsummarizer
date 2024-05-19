from pathlib import Path
import os

import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : %(message)s:')

Project_name = 'TextSummarizer'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{Project_name}/__init__.py",
    f"src/{Project_name}/components/__init__.py",
    f"src/{Project_name}/pipeline/__init__.py",
    f"src/{Project_name}/entity/__init__.py",
    f"src/{Project_name}/constants/__init__.py",
    f"src/{Project_name}/logging/__init__.py",

    f"src/{Project_name}/utils/__init__.py",
    f"src/{Project_name}/utils/common.py",

    f"src/{Project_name}/config/__init__.py",
    f"src/{Project_name}/config/configuration.py",

    "config/config.yaml",
    "params.yaml",
    
    "app.py",
    "main.py",
    "setup.py",

    "Dockerfile",
    "requirements.txt",
    "research/trials.ipynb"
]


for filepath in list_of_files:
    filepath = Path(filepath)

    filedir,filename = os.path.split(filepath)

    #The necessary directories are created if they don't exist.
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory :{filedir} for the filename:{filename}")

    
    #Check if the file does not exist or if it exists but is empty
    if (not os.path.exists(filepath)) or (os.Path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
        logging.info(f"Creating empty file :{filepath}")
    else:
        logging.info(f"File :{filename} already exists")