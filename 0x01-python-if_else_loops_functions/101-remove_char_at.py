#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    cpy_str = ""
    for i in range(len(str)):
        if i != n:
            cpy_str += str[i]
    return cpy_str
