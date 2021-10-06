#!/usr/bin/python3
"""
Function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Function that checks for type errors and
    returns the addition of two cast integers.
    """
    if isinstance(a, bool):
        raise TypeError("a must be an integer")
    if isinstance(b, bool):
        raise TypeError("b must be an integer")
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
