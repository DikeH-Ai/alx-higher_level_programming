#!/usr/bin/python3
for i in range(100):
    if (i % 10) <= abs(i/10):
        continue
    if i not in range(80, 100):
        print("{:02}, ".format(i), end="")
    else:
        print("{:02}".format(i))
