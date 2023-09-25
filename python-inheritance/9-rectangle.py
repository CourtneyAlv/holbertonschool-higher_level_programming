#!/usr/bin/python3
"""Defines a rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    "represents a rectangle"
    def __init__(self, width, height):
        """Inititializes a recatangle
            Args:
            width (int): width of rect
            height (int): height of rect
            """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
