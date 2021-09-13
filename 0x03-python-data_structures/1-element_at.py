#!/usr/bin/python3


def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx > (len(my_list) - 1):
        return None
    for n in range(0, len(my_list)):
        if n == idx:
            return my_list[n]
