#!/usr/bin/python3
"""
a function that returns the JSON representation
of an object (string)
"""
import json


def to_json_string(my_obj):
    """
        Function:
            to_json_string: returns json representation
        Arguments:
            my_obj: python object
        Return:
            json fmt
    """
    return json.dumps(my_obj)
