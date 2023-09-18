#!/urs/bin/python3

"""
Defines base class
"""


class Base:
    """
    Base class: this will be the base of all class in
                task
    private class att = __nb_objects:
                will save al the number of created objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization function for class
        arguments:
            id = gives instance id numbers
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
