#!/usr/bin/python3


def no_c(my_string):

    new = my_string.translate({ord(c): None for c in 'cC'})
    return new
