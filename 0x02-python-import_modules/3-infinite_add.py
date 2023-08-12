#!/usr/bin/python3
import sys
if __name__ == "__main__":
    result = []
    if len(sys.argv) > 1:
        for i in sys.argv[1:]:
            result.append(int(i))
    print(sum(result))
