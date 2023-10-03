#!/usr/bin/python3

"""Define a Square class"""
from models.rectangle import Rectangle


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

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
