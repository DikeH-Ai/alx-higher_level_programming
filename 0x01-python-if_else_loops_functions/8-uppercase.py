#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for i in str:
        if ord(i) in range(97, 123):
            i = ord(i) - 32
            upper += chr(i)
        else:
            upper += i
    print("{}".format(upper))
