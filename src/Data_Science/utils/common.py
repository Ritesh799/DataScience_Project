import os
import yaml
from src.Data_Science import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.
        
    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file loaded successfully from {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a dictionary as a JSON file.
    
    Args:
        path (Path): Path to save the JSON file.
        data (dict): Data to be saved in JSON format.
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

    logger.info(f"JSON file saved at {path}")

@ensure_annotations
def load_json(path: Path):
    """
    Loads a JSON file and returns its content as a dictionary.
    
    Args:
        path (Path): Path to the JSON file.
        
    Returns:
        dict: Content of the JSON file.
    """
    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"JSON file loaded from {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves data to a binary file using joblib.
    
    Args:
        data (Any): Data to be saved.
        path (Path): Path to save the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Data saved as binary file at {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads data from a binary file using joblib.
    
    Args:
        path (Path): Path to the binary file.
        
    Returns:
        Any: Data loaded from the binary file.
    """
    data = joblib.load(path)
    logger.info(f"Data loaded from binary file at {path}")
    return data