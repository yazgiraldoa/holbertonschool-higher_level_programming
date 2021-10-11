#!/usr/bin/python3
"""
Function that returns the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """Function that returns a list of attributes and methods"""
    return dir(obj)
