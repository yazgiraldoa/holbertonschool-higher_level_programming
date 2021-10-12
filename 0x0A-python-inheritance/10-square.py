#!/usr/bin/python3
"""
Add Square inherited class
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

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)


class Square(Rectangle):
    """
            Class Square inherited from Rectangle
            Attributes:
                size(int): size of a square - private attribute.
    """

    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2
