#!/usr/bin/python3
import calculator_1
import sys
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op_list = {'+', '-', '*', '/'}
    if sys.argv[2] not in op_list:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = {'+': calculator_1.add, '-': calculator_1.sub,
          '*': calculator_1.mul, '/': calculator_1.div}
    print("{} {} {} = {}".format(a, sys.argv[2], b, op[sys.argv[2]](a, b)))
