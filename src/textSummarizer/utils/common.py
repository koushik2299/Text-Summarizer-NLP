import os 
from box.exceptions import BoxValueError #yet 
import yaml
from src.textSummarizer.logging import logger
from ensure import ensure_annotations #yet
from box import ConfigBox #yet
from pathlib import Path
from typing import Any  #Yet

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads Yaml files and raises an relavnat exception and return its content as ConfgiBox

    Arg:
    Path of the yaml file 

    Raises: 
    Value Error: if yaml file is empty 
    e: empty file 

    Returns:
    ConfigBox: Configbox type

    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"{path_to_yaml} Yaml file Successfully loaded")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations    
def create_directories(path_to_directories: list,verbose=True):
    """
    Creates Directories
    Args:
    Path 
    raises:
    path not found exceptions
    returns:
    Nothing
    """

    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        
        if verbose:
            logger.info(f"Created Directory at {path}")