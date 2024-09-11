#!/usr/bin/python3

islower = __import__('7-islower').islower


def uppercase(str):
    for c in str:
        if islower(c):
            c = ord(c) - 32
            alpha = chr(c)
            print(f"{alpha}", end="")
        else:
            print(f"{c}", end="")
    print("")
