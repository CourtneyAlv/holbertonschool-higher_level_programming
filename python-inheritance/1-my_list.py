#!/usr/bin/python3
"""defines a class MyList that inherits from list"""


class Mylist(list):
    """Represents a list"""
    def print_sorted(self):
        """ prints a list, but sorted (ascending sort)
                args:
                self (Mylist): The Mylist instance to be sorted and printed
                    """
        print(sorted(self))
