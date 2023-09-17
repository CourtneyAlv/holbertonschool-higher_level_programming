#!/usr/bin/python3
""" Defining a class Square """


class Square:
    """Represent a Square """
    def __init__(self, size=0):
        """ init method initializing a size attribute
                Args:
                size: (obj: int) Size is calulating the area of a square"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        return self.__size**2
