#!/usr/bin/python3
"""
Class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle.
    Attributes:
        size(int): width of a square
        x(int) = position of the square in x
        y(int) = position of the square in y
        id(int): object id given by Base class
    """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter that retrieves size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter that sets the value of size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Method that returns the square string representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} " \
               f"- {self.width}"

    def update(self, *args, **kwargs):
        """Method that updates the values of square"""
        in_args = 0
        for i in range(len(args)):
            in_args = 1
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.width = args[i]
                self.height = args[i]
            elif i == 2:
                self.x = args[i]
            elif i == 3:
                self.y = args[i]
        if in_args == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Method that returns the rectangle dictionary representation"""
        return {"x": self.x, "y": self.y,
                "id": self.id, "size": self.width}
