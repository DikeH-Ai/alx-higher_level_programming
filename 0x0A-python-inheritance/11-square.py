#!/usr/bin/python3
"""
    Defines a square class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
       Square class (subclass) to Rectangle
    """
    def __init__(self, size):
        """
            init method
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Area of a square"""
        return self.__size**2

    def __str__(self):
        """Magic method str(0"""
        return f"[Square] {self.__size}/{self.__size}"
