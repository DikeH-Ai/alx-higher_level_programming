#!/usr/bin/python3
""" a square-printing function."""


def print_square(size):
    """Print a square.

    Arguments:
        size: height/width of the square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
