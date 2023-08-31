#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        real_number = 0
        for i in my_list[ :x]:
            if type(i) is int:
                print("{:d}".format(i), end='')
                real_number += 1
        print()
        return real_number
    except IndexError:
        print("Out of range")
    finally:
        return real_number



if __name__ == "__main__":
    safe_print_list_integers(my_list=[], x=0)
