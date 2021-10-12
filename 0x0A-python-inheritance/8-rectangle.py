#!/usr/bin/python3
"""
Defining inherited class
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


class Rectangle(BaseGeometry):
    """
        Class Rectangle inherited from Base Geometry
        Attributes:
            width(int): width of a rectangle - private attribute.
            height(int): height of a rectangle - private attribute.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
