import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file :{path_to_yaml} loaded successfully")
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info("directory created at :{path}")


@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path,"w") as file:
        json.dump(data,file,indent=4)

    logger.info(f"json file saved at {path}")


@ensure_annotations
def load_json(path:Path)-> ConfigBox:
    with open(path,"r") as file:
        content = json.load(file)
    
    logger.info(f"json file loaded from {path}")
    return content

@ensure_annotations
def save_bin(path:Path,data:Any):
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at {path}")   


@ensure_annotations
def load_bin(path:Path):
    data = joblib.load(filename=path) 
    logger.info(f"binary file loaded from {path}")  
    return data

@ensure_annotations
def get_size(path:Path)->str:
    size =  round(os.path.getsize(path)/1024)
    return f"~{size}KB"

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())