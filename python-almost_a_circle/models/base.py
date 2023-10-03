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

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            json_str = cls.to_json_string([
                obj.to_dictionary() for obj in list_objs
            ])
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """that returns the list of the JSON string rep json_string:"""
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set:"""
        if dictionary and dictionary is not {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy
