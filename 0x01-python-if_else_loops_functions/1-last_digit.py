#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
position = ""
if number >= 0:
    if ((number % 10) > 5):
        position = "and is greater than 5"
    elif (number != 0 and number < 6):
        position = "and is less than 6 and not 0"
    elif (number == 0):
        position = "and is 0"
    print(f"Last digit of {number} is {number % 10} {position}")
else:
    print(f"Last digit of {number} is -{abs(number) % 10}\
    and is less than 6 and not 0")
