#!/usr/bin/python3
"""
Student class
"""


class Student:
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        """Init student and attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dictionary representation of student"""
        student_dict = self.__dict__
        if attrs is None:
            return student_dict

        if (all(isinstance(x, str) for x in attrs)
                and isinstance(attrs, listi)):
            att_dict = [f"{key}: {value}"
                        for key, value in student_dict.items()
                        if key in attrs]

            return att_dict

        return self.__dict__
