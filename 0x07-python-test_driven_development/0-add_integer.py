#!/usr/bin/python3
"""
    add_integer function that returns the addition of arguments
"""


def add_integer(a, b=98):
    """
        add_integer:
            Function returns the addition of two integer/float items
        Arguments:
            a: first integer item
            b: second integer item
        Returns:
            a + b = value
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    add_integer(a, b)
