#!/usr/bin/python3
"""a name function."""


def say_my_name(first_name, last_name=""):
    """Prints first and last name

    Arguments:
        first_name: first name to print.
        last_name: last name to print.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
