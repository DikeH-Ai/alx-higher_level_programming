#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return my_list

    new_list = [i % 2 == 0 for i in my_list]
    return new_list


if __name__ == "__main__":
    divisible_by_2(my_list=[])
