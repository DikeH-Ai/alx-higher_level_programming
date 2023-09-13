#!/usr/bin/python3
"""
Define function to writes and return number of words
"""


def write_file(filename="", text=""):
    """
        Function:
            write_file: writes and return number of words
        Arguments:
            filename: represents the name of the file
            text: srings to be written
        Return:
            Number of words written
    """
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)

    return len(text)
