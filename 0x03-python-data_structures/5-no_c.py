#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        my_string = ''.join([char for char in my_string if char not in "cC"])
    return my_string
