#!/usr/bin/python3
"""
Define function to read and print file to stdout
"""


def read_file(filename=""):
    """
        Function:
            read_file: reads content of a file and prints to stdout
        Arguments:
            filename: represents the name of the file
        Return:
            None, prints file contents
    """
    with open(filename, 'r', encoding="utf-8") as file:
        filedata = file.read()
        print(filedata)
