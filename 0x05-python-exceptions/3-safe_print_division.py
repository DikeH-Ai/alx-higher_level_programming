#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    finally:
        try:
            print("Inside result: {}".format(a / b))
        except ZeroDivisionError:
            print("Inside result: None")


if __name__ == "__main__":
    safe_print_division(a, b)
