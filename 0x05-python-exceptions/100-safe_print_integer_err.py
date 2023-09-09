#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        result = int(value)
        print("{:d}".format(result))
        return True
    except ValueError as e:
        print(f"Exception: {e}", file=sys.stderr)
        return False


if __name__ == "__main__":
    safe_print_integer_err(value)
