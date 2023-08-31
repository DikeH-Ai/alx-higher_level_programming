#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    final_list = []
    try:
        for i in range(list_length):
            try:
                final_list.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                final_list.append(0)
                print("division by 0")
            except IndexError:
                final_list.append(0)
                print("out of range")
            except TypeError:
                final_list.append(0)
                print("wrong type")
    finally:
        return final_list


if __name__ == "__main__":
    list_division(my_list_1, my_list_2, list_length)
