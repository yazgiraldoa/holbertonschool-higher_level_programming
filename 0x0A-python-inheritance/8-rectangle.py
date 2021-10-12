#!/usr/bin/python3
"""
Defining inherited class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Class Rectangle inherited from Base Geometry
        Attributes:
            width(int): width of a rectangle - private attribute.
            height(int): height of a rectangle - private attribute.
    """
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
