#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    list_def = [x for x in dir(hidden_4) if x[0] != '_']
    for i in list_def.sort():
        print(i)
