#!/usr/bin/python3
"""
Verifying attribute in class Square.
"""


class Square:
    """
    Class that defines a square.
    Attributes:
        size(int): size of the square - private attribute.
    """

    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
