#!/usr/bin/python3
"""
Verifying object instantiation
"""


def is_same_class(obj, a_class):
    """
    function that returns True if the object is exactly
    an instance of the specified class
    """
    if type(obj) == a_class:
        return True
    return False
