#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_num = float('-inf')
    for i in my_list:
        if i > max_num:
            max_num = i
    return max_num


if __name__ == "__main__":
    max_integer(my_list=[])
