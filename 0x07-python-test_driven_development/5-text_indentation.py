#!/usr/bin/python3
"""
Function that prints a text with
2 new lines after each delimiter.
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    str_to_print = ""
    for letter in text:
        if letter not in [".", "?", ":"]:
            str_to_print += letter
        else:
            str_to_print += letter
            str_to_print = str_to_print.strip()
            print("{}\n".format(str_to_print))
            str_to_print = ""
    if len(str_to_print) != 0:
        str_to_print = str_to_print.strip()
        print("{}".format(str_to_print), end='')
