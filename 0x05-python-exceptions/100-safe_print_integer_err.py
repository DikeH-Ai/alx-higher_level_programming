#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        if not isinstance(value, int):
            raise ValueError
        print("{:d}".format(value))
        return True
    except ValueError as e:
        print(f"Exception: {e}", file=sys.stderr)
        return False


if __name__ == "__main__":
    safe_print_integer_err(value)
