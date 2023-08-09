#!/usr/bin/python3
alpha = ''
for i in range(97, 123):
    if chr(i) == 'e' or chr(i) == 'q':
        continue
    alpha += chr(i)
print("{}".format(alpha), end="")
