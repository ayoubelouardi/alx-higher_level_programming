#!/usr/bin/python3
for k in range(100):
    if k != 99:
        print("{:02}".format(k), end=", ")
    else:
        print("{:01}".format(k))
