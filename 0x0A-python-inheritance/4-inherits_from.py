#!/usr/bin/python3
"""
Define fuon to check if an object is an instance
of a class
"""


def inherits_from(obj, a_class):
    """
    is_same_class (function): checks if object is
        of the same class
    Argument:
        obj (any type): object i.e(int, list etc.)
        a_class (class): class
    Return:
        returns either True or False
    """
    if type(obj) == a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
