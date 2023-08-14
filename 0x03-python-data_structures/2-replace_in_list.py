#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > (len(my_list) - 1):
        return my_list
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list


if __name__ == "__main__":
    replace_in_list(my_list, idx, element)
