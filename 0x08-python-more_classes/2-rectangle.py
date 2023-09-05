#!/usr/bin/python3
""" CREATE RECTANGLE CLASS """


class Rectangle:
    """ Init Rectangle """
    def __init__(self, width=0, height=0):
        """
        This is a docstring for the constructor (__init__) method.
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Width Getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter method"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """height Getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """Area instance method"""
        return self.__height * self.__width

    def perimeter(self):
        """perimeter instance method"""
        if (self.__width == 0) or (self.__height == 0):
            return 0
        else:
            return 2 * (self.__height + self.__width)
