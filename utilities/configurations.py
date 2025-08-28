import configparser
from pathlib import Path
import json

def get_config():
    config_parser = configparser.ConfigParser()
    config_parser.read("properties.ini")
    return config_parser

def read_json(file_name):
    # Get the project root by going up one level from the utilities folder
    project_root = Path(__file__).parent.parent.absolute()
    test_data_path = project_root/"data"/file_name
    with open(test_data_path) as j:
        data = json.load(j)
        return data
