#!/usr/bin/python3
"""
Class Student with public method to_json and
method reload_from_json
"""


class Student:
    """
    Class Student that has a method to print dict
    representation of a Student instance.
    Attributes:
        first_name(str): student's first name
        last_name(str): student's last name
        age(int): student's age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        all_attr = self.__dict__.copy()

        if isinstance(attrs, list):
            for key in self.__dict__.keys():
                if key not in attrs:
                    del all_attr[key]
        return all_attr

    def reload_from_json(self, json):
        for key, value in json.items():
            if key == "first_name":
                self.first_name = value
            if key == "last_name":
                self.last_name = value
            if key == "age":
                self.age = value
