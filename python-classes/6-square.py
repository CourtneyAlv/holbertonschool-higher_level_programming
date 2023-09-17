#!/usr/bin/python3
""" Defining a class Square """


class Square:
    """Represent a Square """
    def __init__(self, size=0, position=(0, 0)):
        """ init method initializing a size attribute
                Args:
                size: (obj: int) Size is calulating the area of a square
                position: represents a point or a location and stored in a
                tuple"""

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            TypeError('position must be a tuple of 2 positive integers')
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x <= 0 or y <= 0:
            TypeError('position must be a tuple of 2 positive integers')
        self.__postion = value

    def area(self):
        return self.__size**2

    def my_print(self):
        # _ is a placeholder for a variable that you dont need in a loop
        if self.__size == 0:
            print("")
            return
        else:
            x, y = self.__position
            for _ in range(y):
                print()
            for _ in range(self.__size):
                print('-' * x + '#' * self.__size)
