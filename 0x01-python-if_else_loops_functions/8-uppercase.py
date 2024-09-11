#!/usr/bin/python3

islower = __import__('7-islower').islower


def uppercase(str):
    for c in str:
        if islower(c):
            c = ord(c) - 32
            alpha = chr(c)
            print("{}".format(alpha), end="")
        else:
            print("{}".format(c), end="")
    print("")
