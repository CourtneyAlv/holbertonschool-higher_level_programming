#!/usr/bin/python3

"""Define a base class model"""
import json


class Base:
    """ Represent a Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor for the base class

            Args:
                id (int): integer representing the id
            """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ that returns the JSON string rep. of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
