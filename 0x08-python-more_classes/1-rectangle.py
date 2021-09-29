#!/usr/bin/python3
"""
Defining two attributes for a class.
"""


class Rectangle:
    """
    Class that defines a rectangle.
    Attributes:
        width(int): width of a rectangle - private attribute.
        height(int): height of a rectangle - private attribute.
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property that retrieves width"""
        return self.__width

    @property
    def height(self):
        """Property that retrieves height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Property setter that sets the value of width"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        """Property setter that sets the value of height"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")
