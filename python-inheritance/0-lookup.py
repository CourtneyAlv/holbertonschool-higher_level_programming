#!/usr/bin/python3

"""Returning a list Object"""


def lookup(object):
    """Return a list of avaliable attributes and methods
            Args:
            obj(object): The object to inspect
            Returns:
            list: A list of attributes and method names"""
    attributes_and_methods = dir(object)
    return attributes_and_methods
