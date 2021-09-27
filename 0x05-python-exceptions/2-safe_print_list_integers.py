#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    len_list = 0

    for element in range(0, x):
        try:
            print("{:d}".format(my_list[element]), end='')
            len_list += 1
        except TypeError:
            pass
        except ValueError:
            pass
    print('\n', end='')
    return len_list
