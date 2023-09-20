#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """ A function that prints your first and last name
        :first_name: (str) first argument
        :last_name: (str) second argument
        return: None"""

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print("My name is {} {}".format(first_name, last_name))
