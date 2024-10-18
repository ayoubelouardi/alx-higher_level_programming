#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    if argc == 0:
        print("{} argument:".format(argc))
    else:
        print("{} argument:".format(argc))
    for i in range(1, argc + 1):
        print("{}: {}".format(i, sys.argv[i]))
