#!/usr/bin/python3
for c in range(26):
    if c == 4 or c == 16:
        continue
    print("{:c}".format(c+97), end="")
