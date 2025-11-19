#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if j == matrix[i][j]:
                print("{:d}".format(j),end="\n")
            else:
                print("{:d}".format(j), end=" ")
