#!/usr/bin/python3
import json
"""
a function that returns the JSON representation
of an object (string)
"""


def from_json_string(my_str):
    """
        Function:
            to_json_string: returns json representation
        Arguments:
            my_obj: python object
        Return:
            json fmt
    """
    return json.loads(my_str)
