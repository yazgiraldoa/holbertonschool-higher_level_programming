#!/usr/bin/python3
"""
Class Student with public method to_json
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

    def to_json(self):
        return self.__dict__
