#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = sys.argv[2]
    if op == '+':
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == '-':
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif op == '*':
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif op == '/':
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print("{} / {} = {}".format(sys.argv[1], sys.argv[3], div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
