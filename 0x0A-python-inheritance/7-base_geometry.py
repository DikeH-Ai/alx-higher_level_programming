#!/usr/bin/python3
"""
    Defines a geomerty class
"""


class BaseGeometry:
    """
        Geometry class
    """
    def area(self):
        """
        Method that defines area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator: validates data

        argument:
            name: refers to name
            value: item value
        """
        if type(value) !=  int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
