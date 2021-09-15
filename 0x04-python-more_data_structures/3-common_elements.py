#!/usr/bin/python3


def common_elements(set_1, set_2):
    new_set = {value for value in set_1 if value in set_2}
    return new_set
