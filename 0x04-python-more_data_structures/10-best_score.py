#!/usr/bin/python3
def best_score(a_dictionary):
    max_stud = 0
    if a_dictionary is None or (len(a_dictionary) == 0):
        return None

    for x, y in a_dictionary.items():
        if y >= max_stud:
            max_stud = y
            max_name = x
    return max_name


if __name__ == "__main__":
    best_score(a_dictionary={})
