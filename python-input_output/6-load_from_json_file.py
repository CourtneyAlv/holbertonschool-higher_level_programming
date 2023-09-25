#!/usr/bin/python3
"""function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”
    Args:
        filename (str): name of json file to load

        Returns:
            object: object created from json file
        """
    with open(filename, 'r') as file:
        obj = json.load(file)
    return obj
