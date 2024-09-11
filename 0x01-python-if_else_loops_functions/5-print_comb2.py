#!/usr/bin/python3
for k in range(100):
    if k != 99:
        print("{:00}".format(k), end=", ")
    else:
        print("{:00}".format(k))
