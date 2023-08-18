#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        a_dicitionary = {}
        return a_dictionary

    new_dict = {x: y * 2 for x, y in a_dictionary.items()}
    return new_dict


if __name__ == "__main__":
    multiply_by_2(a_dictionary)
