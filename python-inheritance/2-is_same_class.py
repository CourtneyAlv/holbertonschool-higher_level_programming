#!/usr/bin/python3

def is_same_class(obj, a_class):
    """Returns True If the object is exactly an instance of the specifed class
    otherwise False
        Args:
        obj: the object to be checked
        a_class: The class to compare the object with

        Returns:
            bool: True if obj is an instance of a_class, False if not
            """
    return type(obj) is a_class
