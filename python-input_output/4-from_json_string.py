#!/usr/bin/python3
"""function that returns an object (Python data structure) represented
by a JSON string:"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string:
        Args:
            my_str (str): a json-formatted string.
        Returns:
            object: Python data represented by the json str
        """
    try:
        return json.loads(my_str)
    except json.JSONDecodeError:
        return None
