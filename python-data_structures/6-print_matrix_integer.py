#!/usr/bin/python3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if j == len(row) - 1:
                print("{:d}".format(matrix[i][j]), end="\n")
            else:
                print("{:d}".format(matrix[i][j]), end=" ")
