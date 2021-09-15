#!/usr/bin/python3


def uniq_add(my_list=[]):

    sum = 0
    uniq_set = set(my_list)

    for number in uniq_set:
        sum += number
    return sum
