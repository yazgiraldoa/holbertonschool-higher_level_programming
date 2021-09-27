#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len_list = 0
    try:
        for element in range(0, x):
            print("{}".format(my_list[element]), end='')
            len_list += 1
        print('\n', end='')
    except IndexError:
        print('\n', end='')
        return len_list
    return len_list
