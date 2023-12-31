#!/usr/bin/python3
"""
load_from_json_file: converts json
to py obj
"""
import json


def load_from_json_file(filename):
    """
        Function:
            load_from_json_file: converts json
            to py obj
        Arguments:
            filename: file name
        Return:
            object
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
