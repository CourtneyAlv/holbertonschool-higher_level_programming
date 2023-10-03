#!/usr/bin/python3
from models.rectangle import Rectangle
"""Define a Square class"""


class Square(Rectangle):
    """Inherits from rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor
            Args:
                size (int): the size of the new square
                x (int): the x coordinate of the new square
                y (int): the y coordinate of the new square
                id (int): integer representing id of the new square
            """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overloads __str__ method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
