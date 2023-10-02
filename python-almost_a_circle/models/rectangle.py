#!/usr/bin/python3

"""Define a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """ Represents a rectangle/ inherited from class Base """

    def __init__(self, width, height, x=0, y=0, id=None):

        self.__width = width    # private attrubutes ↆ
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)
