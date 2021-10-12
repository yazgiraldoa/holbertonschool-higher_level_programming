#!/usr/bin/python3
"""
Function that reads a text file (UTF8)
and prints it to stdout
"""


def read_file(filename=""):
    """Function that reads a file and prints its content"""
    with open(filename, encoding='utf-8') as f:
        read_data = f.read()
        print(read_data, end='')
