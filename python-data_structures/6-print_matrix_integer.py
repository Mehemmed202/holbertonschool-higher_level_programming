#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(0, len(row)):
            if row[i] == row[-1]:
                print("{:d}".format(row[i]), end="\n")

            else:
                print("{:d}".format(row[i]), end=" ")
