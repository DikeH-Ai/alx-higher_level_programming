#!/usr/bin/python3
""" Python super and sub class prnit list"""


class MyList(list):
    """
    Mylist: sub class to print superclass list
    Argument:
        list : a super class
    """

    def print_sorted(self):
        """
        Prints list
        """
        print(sorted(self))
