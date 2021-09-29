#!/usr/bin/python3
"""
Add attribute in class Square.
"""


class Square:
    """
    Class that defines a square.
    Attributes:
        size(int): size of the square - private attribute.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property that retrieves size"""
        return self.__size

    @property
    def position(self):
        """Property that retrieves position"""
        return self.__position

    @size.setter
    def size(self, value):
        """Property setter that sets the value of size"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, value):
        """Property setter that sets the position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if isinstance(value[0], int) and isinstance(value[1], int):
            if value[0] >= 0 and value[1] >= 0:
                self.__position = value
            else:
                raise TypeError("position must be a tuple "
                                "of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Public instance method that prints the square with character #"""
        if self.__size == 0:
            print()
            return

        line = 0
        while line < self.__position[1]:
            print()
            line += 1

        i = 1
        while i <= self.__size:
            j, k = 1, 1
            while k <= self.__position[0]:
                print(" ", end='')
                k += 1
            while j <= self.__size:
                print("#", end='')
                j += 1
            print()
            i += 1
