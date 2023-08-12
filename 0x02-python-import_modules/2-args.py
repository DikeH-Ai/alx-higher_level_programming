#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) - 1 == 0:
        print(f"{len(sys.argv) - 1} arguments.")
    else:
        print(f"{len(sys.argv) - 1} arguments:")
        for i, item in enumerate(sys.argv):
            if i != 0:
                print(f"{i}: {item}")
