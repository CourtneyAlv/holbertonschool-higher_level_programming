#!/usr/bin/python3
"""defines True if the object is an instance of, or if the object is an
instance of a class that inherited from, the specified class;
otherwise False."""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of, or if the object is an
instance of a class that inherited from, the specified class;
otherwise False.
    Args:
        obj: the object to be checked.
        a_class: The class to compare the object with.

        Returns:
            bool: True if obj is an instance of a_class
            or  False otherwise"""
    return isinstance(obj, a_class)
