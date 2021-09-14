#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    num1 = 0
    num2 = 0

    if len(tuple_a) >= 2:
        if len(tuple_b) >= 2:
            num1 = tuple_a[0] + tuple_b[0]
            num2 = tuple_a[1] + tuple_b[1]
        elif len(tuple_b) == 1:
            num1 = tuple_a[0] + tuple_b[0]
            num2 = tuple_a[1]
        elif len(tuple_b) == 0:
            num1 = tuple_a[0]
            num2 = tuple_a[1]
    if len(tuple_a) == 1:
        if len(tuple_b) >= 2:
            num1 = tuple_a[0] + tuple_b[0]
            num2 = tuple_b[1]
        elif len(tuple_b) == 1:
            num1 = tuple_a[0] + tuple_b[0]
            num2 = 0
        elif len(tuple_b) == 0:
            num1 = tuple_a[0]
            num2 = 0
    if len(tuple_a) == 0:
        if len(tuple_b) >= 2:
            num1 = tuple_b[0]
            num2 = tuple_b[1]
        elif len(tuple_b) == 1:
            num1 = tuple_b[0]
            num2 = 0
        elif len(tuple_b) == 0:
            num1 = 0
            num2 = 0
    new_tuple = num1, num2
    return new_tuple
