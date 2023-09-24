#!/usr/bin/python3
"""Defines a function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class ;
otherwise False."""


def inherits_from(obj, a_class):
    """returns a function that returns True if the object is an instance of
    a class that inherited (directly or indirectly) from the specified class ;
    otherwise False.
        Args:
            obj: The object to be checked
            a_class: The class to compare the object with
        Returns:
             bool: True if obj is instance, otherwise False"""
    return isinstance(obj, a_class) and type(obj) is not a_class
