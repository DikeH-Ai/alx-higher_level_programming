#!/urs/bin/python3

"""
Defines base class
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Function returns Json strings"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json to file"""
        name = cls.__name__ + ".json"
        with open(name, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                class_list = [x.to_dictionary() for x in list_objs]
                f.write(Base.to_json_string(class_list))

    @staticmethod
    def from_json_string(json_string):
        """convert json to strings"""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with attributes set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(2, 2)
            else:
                dummy = cls(1, 1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """
            returns a list of instances from file
        """
        name = f"{cls.__name__}.json"
        try:
            with open(name, "r") as f:
                list_value = json.load(f)
                return [cls.create(**x) for x in list_value]
        except FileNotFoundError:
            return []
