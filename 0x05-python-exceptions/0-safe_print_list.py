#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        real_number = 0
        for i in my_list[:x]:
            print(i, end='')
            real_number = real_number + 1
    except IndexError:
        pass
    finally:
        print()
        return real_number


if __name__ == "__main__":
    safe_print_list(my_list=[], x=0)
