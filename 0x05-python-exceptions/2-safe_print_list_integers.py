#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    real_number = 0
    for i in my_list[:x]:
        try:
            print("{:d}".format(i), end='')
            real_number += 1
        except (IndexError, TypeError):
            pass
    print()
    return real_number


if __name__ == "__main__":
    safe_print_list_integers(my_list=[], x=0)
