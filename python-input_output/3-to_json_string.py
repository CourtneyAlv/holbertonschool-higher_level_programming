#!/usr/bin/python3
"""function that returns the JSON representation of an object (string)"""

import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string):
        Args:
            my_obj: object to be converted to Json

            Returns:
            str: The Json rep of the object
            """
    return json.dumps(my_obj)
