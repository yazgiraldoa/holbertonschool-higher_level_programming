#!/usr/bin/python3
"""
Function that appends a string at the end of file (UTF8) and
returns the number of characters added
"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of file"""
    with open(filename, mode='a', encoding='utf-8') as f:
        num_char_written = f.write(text)
    return num_char_written
