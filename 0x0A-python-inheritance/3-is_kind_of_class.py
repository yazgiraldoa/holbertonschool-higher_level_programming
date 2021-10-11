#!/usr/bin/python3
"""
Verifying object instantiation or inheritance
"""


def is_kind_of_class(obj, a_class):
    """
    Function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from.
    """
    if isinstance(obj, a_class):
        return True
    return False
