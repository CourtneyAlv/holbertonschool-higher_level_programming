#!/usr/bin/python3

"""Define a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """ Represents a rectangle/ inherited from class Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor
            Args:
                width (int): the width of the new rectangle
                height (int): the height of the new rectangle
                x (int): the x coordinate of the new rectangle
                y (int): the y coordinate of the new rectange
                id (int): intger representing id of the new rectangle
            """
        self.width = width    # private attrubutes ↆ
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        # Getter and setters for width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return the area of a rectangle """
        return self.width * self.height

    def display(self):
        """Prints in stdout the rect. instance with char '#' """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns/overrides the string rep of Rectangle"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - " \
            f"{self.width}/{self.height}"

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
            arg_name = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, arg_names[i], value)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
