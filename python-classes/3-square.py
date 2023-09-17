#!/usr/bin/python3
""" Defining a class Square """


class Square:
    """Represent a Square """
    def __init__(self, size=0):
        """ init method initializing a size attribute
                Args:
                size: (obj: int) Size is calulating the area of a square"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        return self.__size**2
