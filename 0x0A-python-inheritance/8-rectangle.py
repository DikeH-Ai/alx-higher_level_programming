#!/usr/bin/python3
"""
    Defines a geomerty class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Rectangle class (subclass) to BaseGeometry
    """
    def __init__(self, width, height):
        """
            init method
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
