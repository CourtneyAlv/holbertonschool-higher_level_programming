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

    def update(self, *args, **kwargs):
        """ update Rect. class by assigning an argument to each attribute"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        if args:
            arg_name = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, arg_name[i], value)
        for key, value in kwargs.items():
            setattr(self, key, value)

        def to_dictionary(self):
            """ Returns the dictionary representation of a Square """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y,
        }
