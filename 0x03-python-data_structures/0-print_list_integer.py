#!/usr/bin/python3
def print_list_integer(my_list=[]):
    txt = "{}"
    for i in range(0, len(my_list)):
        print(txt.format(my_list[i]))
