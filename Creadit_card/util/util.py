import yaml
from Creadit_card.exception import CreaditException
import os, sys

def read_yaml_file(file_path:str):
    """
    Read yaml file and return the content in a dictionary.
    file_path:str
    """
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise CreaditException(e,sys)