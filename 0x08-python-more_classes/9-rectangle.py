#!/usr/bin/python3
"""
Add class method to a class.
"""


class Rectangle:
    """
    Class that defines a rectangle.
    Attributes:
        width(int): width of a rectangle - private attribute.
        height(int): height of a rectangle - private attribute.
        number_of_instances(int): count the number of instances existing
        print_symbol(any): symbol used to print a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

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

    def area(self):
        """Public instance method that returns rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method that returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Standard method that returns the rectangle with character #"""

        rectangle = ""

        if self.__width == 0 or self.__height == 0:
            return rectangle

        i = 1
        while i <= self.__height:
            rectangle += str(self.print_symbol) * self.__width
            if i < self.__height:
                rectangle += '\n'
            i += 1
        return rectangle

    def __repr__(self):
        """Standard method that returns string representation of rectangle"""
        return "Rectangle(" + str(self.__width) + \
               ", " + str(self.__height) + ")"

    def __del__(self):
        """Destructor method that prints a str when object is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method that returns the biggest rectangle based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        elif rect_1.area() == rect_2.area():
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Class method that returns new Rectangle
        instance with width == height == size"""
        new_rectangle = cls(size, size)
        return new_rectangle
