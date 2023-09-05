#!/usr/bin/python3
""" CREATE RECTANGLE CLASS """


class Rectangle:
    """ Init Rectangle """
    def __init__(self, width=0, height=0):
        """
        This is a docstring for the constructor (__init__) method.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
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

    def __str__(self):
        rect = ""
        if (self.__height == 0) or (self.__width == 0):
            return ""
        rect_char = '#'
        for _ in range(self.__height):
            rect += rect_char * self.__width + "\n"
        return rect
