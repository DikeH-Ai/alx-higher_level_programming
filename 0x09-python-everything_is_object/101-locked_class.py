#!/usr/bin/python3
"""Locked class"""


class LockedClass:
    """ LOCKED CLASS"""

    def __setattr__(self, name, value):
        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError(
                """'LockedClass' object has no attribute 'last_name'""")
