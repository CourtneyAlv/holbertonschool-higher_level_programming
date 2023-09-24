#!/usr/bin/python3
"""Defines an empty class"""


class BaseGeometry:
    """Defines an empty class"""
    def area(self):
        """ Computes the area of the geometry
            The method is not implemented in the base class
            Raises
                Exception: raise exception if are() id not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer value
            Args:
                name (str): whats being validated
                value (int): the value to be validated
            Raises:
                TypeError: if not an int
                ValueError: if less than or equal to 0
                """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
