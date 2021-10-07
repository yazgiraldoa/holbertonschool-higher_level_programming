#!/usr/bin/python3
"""
Function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Function divides all elements of a matrix, save the
    results in a new matrix and returns the new matrix.
    """

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not isinstance(div, (float, int)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    past_row_len = 0
    for row in matrix:

        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")

        current_row_len = len(row)
        if past_row_len != 0 and past_row_len != current_row_len:
            raise TypeError("Each row of the matrix must have the same size")
        else:
            past_row_len = current_row_len

        for element in row:
            if not isinstance(element, (float, int)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
            if isinstance(element, bool):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")

    new_matrix = [[round((i / div), 2) for i in row] for row in matrix]
    return new_matrix
