#!/usr/bin/python3
""" function that returns the dictionary description with simple data structure
"""
import json


def class_to_json(obj):
    """converts an object to a dictionary for json
        Args:
            obj: instance of a class
        Returns:
            dict: dictionary rep
        """
    if not hasattr(obj, '__dict__'):
        raise TypeError("object must have '__dict__ attribute for serializing")

    seraialized_data = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serialized_data[key] = value
    return serialized_data
