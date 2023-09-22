#!/usr/bin/python3
"""
Defines Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class: this class defines a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initialization function

            Parameters:
            - `width` (int): The width of the Rectangle being created.
            - `height` (int): The height of the Rectangle being created.
            - `x` (int): The x-coordinate of the Rectangle being created.
            - `y` (int): The y-coordinate of the Rectangle being created.
            - `id` (int): The unique identifier of the Rectangle being created.
        """
        self.is_valid1(width, "width")
        self.is_valid1(height, "height")
        self.is_valid2(x, "x")
        self.is_valid2(y, "y")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @staticmethod
    def is_valid1(value, name=""):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    @staticmethod
    def is_valid2(value, name=""):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        """get the width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width value"""
        self.is_valid1(value, "width")
        self.__width = value

    @property
    def height(self):
        """get the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height value"""
        self.is_valid1(value, "height")
        self.__height = value

    @property
    def x(self):
        """get the x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x value"""
        self.is_valid2(value, "x")
        self.__x = value

    @property
    def y(self):
        """get the y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y value"""
        self.is_valid2(value, "y")
        self.__y = value

    def area(self):
        """Returns area"""
        return self.__height * self.__width

    def display(self):
        """Prints rectangle using # symbol"""
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        for _ in range(self.y):
            print()

        for _ in range(self.__height):
            print(" " * self.x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """Update attributes"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns instance info"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self) -> str:
        """return string rep"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.__width}/{self.__height}"
