#!/usr/bin/python3
"""
Class Rectangle that
inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle that inherits from Base
    Attributes:
        width(int): width of a rectangle
        height(int): height of a rectangle
        x(int) = position of the rectangle in x
        y(int) = position of the rectangle in y
        id(int): object id given by Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter that retrieves width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter that sets the value of width"""
        if isinstance(value, int) and not isinstance(value, bool):
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Getter that retrieves height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter that sets the value of height"""
        if isinstance(value, int) and not isinstance(value, bool):
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """Getter that retrieves x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter that sets the value of x"""
        if isinstance(value, int) and not isinstance(value, bool):
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """Getter that retrieves y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter that sets the value of y"""
        if isinstance(value, int) and not isinstance(value, bool):
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """Public instance method that returns rectangle area"""
        return self.__height * self.__width

    def display(self):
        """Method that returns the rectangle with character #"""
        line = 0
        while line < self.__y:
            print()
            line += 1

        i = 1
        while i <= self.__height:
            j, k = 1, 1
            while k <= self.__x:
                print(" ", end='')
                k += 1
            while j <= self.__width:
                print("#", end='')
                j += 1
            print()
            i += 1

    def __str__(self):
        """Method that returns the rectangle string representation"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} " \
               f"- {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Method that updates the values of rectangle"""
        in_args = 0
        for i in range(len(args)):
            in_args = 1
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.__width = args[i]
            elif i == 2:
                self.__height = args[i]
            elif i == 3:
                self.__x = args[i]
            elif i == 4:
                self.__y = args[i]
        if in_args == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value

    def to_dictionary(self):
        """Method that returns the rectangle dictionary representation"""
        return {"x": self.__x, "y": self.__y, "id": self.id,
                "height": self.__height, "width": self.__width}
