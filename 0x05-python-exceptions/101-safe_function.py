#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except (IndexError, ZeroDivisionError, ValueError, TypeError) as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None


if __name__ == "__main__":
    safe_function(fct, *args)
