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
    return obj.__dict__
