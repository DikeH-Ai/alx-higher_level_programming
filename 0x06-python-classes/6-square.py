#!/usr/bin/python3
""" Square class with an Area functionality. """


class Square:
    """
    Square class with attributes, methods, setter & getters
    """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) is not tuple and len(position) != 2:
            raise TypeError("""position must be a tuple of 2 positive\
                                    integers""")
        if type(position[0]) is not int and type(position[1]) is not int:
            raise TypeError("""position must be a tuple of 2 positive\
                                    integers""")
        self.__position = position

    def area(self):
        return self.__size**2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple and len(value) != 2:
            raise TypeError("""position must be a tuple of 2 positive\
                                    integers""")
        if type(value[0]) is not int and type(value[1]) is not int:
            raise TypeError("""position must be a tuple of 2 positive\
                                    integers""")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("_" * self.__position[0], end='')
            print("#" * self.__size)
