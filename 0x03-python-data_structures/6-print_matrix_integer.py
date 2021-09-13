#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    if matrix:
        for row in matrix:
            for element in range(len(row)):
                print("{:d}".format(row[element]), end='')
                if element < (len(row) - 1):
                    print("{}".format(' '), end='')
            print("{}".format(''))
