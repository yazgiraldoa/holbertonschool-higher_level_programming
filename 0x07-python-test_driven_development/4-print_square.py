#!/usr/bin/python3
"""
Function that prints a square with the character #.
"""


def print_square(size):
    """
    Function that prints a square with the character #.
    Size must be an integer and > 0
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    i = 1
    while i <= size:
        j = 1
        while j <= size:
            print("#", end='')
            j += 1
        print()
        i += 1
