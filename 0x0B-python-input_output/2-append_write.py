#!/usr/bin/python3
"""
Define function that appends to a file
"""


def append_write(filename="", text=""):
    """
        Function:
            append_write: writes and return number of words
                            appended
        Arguments:
            filename: represents the name of the file
            text: srings to be written
        Return:
            Number of words appended
    """
    with open(filename, 'a+', encoding="utf-8") as file:
        file.write(text)

    return len(text)
