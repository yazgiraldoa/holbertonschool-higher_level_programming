#!/usr/bin/python3
"""
Function that writes a string to a text file (UTF8) and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """Function that writes a text to a file"""
    with open(filename, mode='w', encoding='utf-8') as f:
        num_char_written = f.write(text)
    return num_char_written
