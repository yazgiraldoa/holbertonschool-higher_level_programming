#!/usr/bin/python3
"""
Class Base
"""
import json
import turtle
from time import sleep


class Base:
    """
    Class Base
    Attributes:
        nb_objects(int): number of objects - private class attribute
        id(int): object id - public instance attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that returns the JSON string
        representation of a list of dictionaries"""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Static method that returns the list of
        the JSON string representation json_string"""
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes the JSON string
            representation of list_objs to a file"""
        list_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                dict_to_save = obj.to_dictionary()
                list_dicts.append(dict_to_save)
            list_dicts = Base.to_json_string(list_dicts)
        else:
            list_dicts = str(list_dicts)

        with open(f"{cls.__name__}.json", mode='w', encoding='utf-8') as f:
            f.write(list_dicts)

    @classmethod
    def create(cls, **dictionary):
        """Class method that returns an instance
        with all attributes already set"""
        r1 = cls.__name__
        if cls.__name__ == "Rectangle":
            r1 = cls.__mro__[0](1, 2)
            r1.update(**dictionary)
        elif cls.__name__ == "Square":
            r1 = cls.__mro__[0](2)
            r1.update(**dictionary)
        return r1

    @classmethod
    def load_from_file(cls):
        """Class method that returns a list of instances"""
        obj_list = []
        try:
            with open(f"{cls.__name__}.json", encoding='utf-8') as f:
                str_list_dict = f.read()
                list_dict = cls.from_json_string(str_list_dict)
                for dic in list_dict:
                    obj = cls.create(**dic)
                    obj_list.append(obj)
                return obj_list
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        for shape in list_rectangles:
            t = turtle.Turtle()
            t.pencolor("blue")
            t.up()
            t.goto(shape.x, shape.y)
            t.down()
            t.forward(shape.width)
            t.left(90)
            t.forward(shape.height)
            t.left(90)
            t.forward(shape.width)
            t.left(90)
            t.forward(shape.height)
            sleep(0.5)
            t.clear()
        for shape in list_squares:
            t = turtle.Turtle()
            t.pencolor("red")
            t.up()
            t.goto(shape.x, shape.y)
            t.down()
            t.forward(shape.width)
            t.left(90)
            t.forward(shape.height)
            t.left(90)
            t.forward(shape.width)
            t.left(90)
            t.forward(shape.height)
            sleep(0.5)
            t.clear()
        turtle.done()
