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

        if ((isinstance(attrs, list))
                and all(type(x) is str for x in attrs)):
            att_dict = {key: getattr(self, key)
                        for key in attrs
                        if hasattr(self, key)}

            return att_dict

        return self.__dict__
