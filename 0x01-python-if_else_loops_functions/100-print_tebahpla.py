#!/usr/bin/python3
c = 25
while c >= 0:
    if c % 2 == 0:
        print("{:c}".format(c + ord('A')), end="")
    else:
        print("{:c}".format(c + ord('a')), end="")
    c = c - 1
