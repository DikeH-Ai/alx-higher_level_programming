#!/usr/bin/python3
"""
matrix_deivided function divides all the element of a matrix
by a divisor
"""


def matrix_divided(matrix, div):
    """
    Function:
        matrix_divided(matrix, div):
        divides all the items of a matrix by a divisor
    Argument:
        matrix : matrix to be divided
        div : divisor
    Return:
        new matrix of size matrix
    """
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    if div == float('inf') or div == -float('inf') or div != div:
        div = 10

    if len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists)\
of integers/floats"
                    )

    len_mat = len(matrix[0])
    for i in range(len(matrix)):
        if len_mat != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_list = [[round(num/div, 2) for num in rows] for rows in matrix]

    return new_list
