#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = sys.argv[2]
    match op:
        case '+':
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            print("{} + {} = {}".format(sys.argv[1], sys.argv[3], add(a, b)))
        case '-':
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            print("{} - {} = {}".format(sys.argv[1], sys.argv[3], sub(a, b)))
        case '*':
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            print("{} * {} = {}".format(sys.argv[1], sys.argv[3], mul(a, b)))
        case '/':
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            print("{} / {} = {}".format(sys.argv[1], sys.argv[3], div(a, b)))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
