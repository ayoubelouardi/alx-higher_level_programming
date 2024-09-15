#!/usr/bin/python3
import sys

argc = len(sys.argv) - 1

if argc == 0:
    print("{} arguments.".format(argc))
else:
    print("{} arguments:".format(argc))
for i in range(1, argc + 1):
    print("{}: {}".format(i, sys.argv[i]))
