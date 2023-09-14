#!/usr/bin/python3
"""
Defining a script that takes iin arguments, stores them in a list
and converts them to json
"""
import json
import sys
if __name__ == "__main__":
    s2jf = __import__('5-save_to_json_file').save_to_json_file
    lfjf = __import__('6-load_from_json_file').load_from_json_file

    try:
        py_list = lfjf("add_item.json")
    except FileNotFoundError:
        py_list = []

    py_list.extend(sys.argv[1:])
    s2jf(py_list, "add_item.json")
