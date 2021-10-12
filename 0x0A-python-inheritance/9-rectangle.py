#!/usr/bin/python3
"""
Add str and area methods to inherited class
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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
