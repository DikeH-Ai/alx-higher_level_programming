#!/usr/bin/python3
import json
"""
 a function that writes an Object to a text file
 using a JSON representation:
"""


def save_to_json_file(my_obj, filename):
    """
        Function:
            save_to_json_file: writes an object
                    to file
        Arguments:
            my_obj: python object
            filename: file name
        Return:
            file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
