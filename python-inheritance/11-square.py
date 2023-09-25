#!/usr/bin/python3
"""Define a square"""
Square = __import__('10-square').Square
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents a Square"""
    def __init__(self, size):
        """Initializes a Square
            Args:
            size (int): the size of the square
            """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return ("[Square] {}"
                "/{}").format(self._Rectangle__width, self._Rectangle__height)
