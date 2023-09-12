#!/usr/bin/python3
"""
Define fuon to check if an object is an instance
of a class
"""


def is_kind_of_class(obj, a_class):
    """
    is_same_class (function): checks if object is
        of the same class
    Argument:
        obj (any type): object i.e(int, list etc.)
        a_class (class): class
    Return:
        returns either True or False
    """

    if isinstance(obj, bool):
        return False
    if isinstance(obj, a_class):
        return True
    else:
        return False
