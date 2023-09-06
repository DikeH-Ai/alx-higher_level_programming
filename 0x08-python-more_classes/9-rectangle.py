#!/usr/bin/python3
""" CREATE RECTANGLE CLASS """


class Rectangle:
    """ Init Rectangle """

    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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
        """Return string rep """
        rect_row = ""
        if (self.__height == 0) or (self.__width == 0):
            return ""
        rect_row = str(self.print_symbol) * self.__width
        rect = (rect_row + "\n") * (self.__height - 1) + rect_row
        return rect

    def __repr__(self):
        """Returns an expression in str format"""
        rep_fmt = "Rectangle(" + str(self.__width)
        rep_fmt += ", " + str(self.__height) + ")"
        return rep_fmt

    def __del__(self):
        """detect the deletion of an instance of rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Function returns bigger rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        rect1 = rect_1.area()
        rect2 = rect_2.area()
        if rect1 == rect2:
            return rect_1
        if rect1 > rect2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        rect_inst = cls(size, size)
        return rect_inst
