#!/usr/bin/python3
"""
Defining integer_validator of class Base Geometry
"""


class BaseGeometry:
    """
    Class Base Geometry with public instance method area
    and integer validation
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
