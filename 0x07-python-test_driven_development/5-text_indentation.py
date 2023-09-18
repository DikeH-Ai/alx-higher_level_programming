#!/usr/bin/python3
"""text-indentation function."""


def text_indentation(text):
    """
    print two new lines after each symbol '.', '?', and ':'.
    Arguments:
        text : text to print.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    count = 0
    for i in text:
        if i in ('.', '?', ':') or i == '\n':
            if i == '\n':
                print('\n', end='')
            else:
                print(i.lstrip()+'\n\n', end='')
                count = 1
        elif count == 1:
            print(i.rstrip(), end='')
            count = 0
        else:
            print(i, end='')
