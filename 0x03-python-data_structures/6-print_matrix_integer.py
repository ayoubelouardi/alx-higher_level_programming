#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = len(matrix)
    for row in matrix:
        r_len = len(row)  # take the len of each row
        for i in range(0, r_len):
            print("{:d}".format(row[i]), end="")
            if i is not r_len - 1:
                print(" ", end="")
        print("")
