#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    my_matrix = []
    for row in matrix:
        my_matrix.append(row)
        mlist = []
        for i in row:
            mlist.append(i * i)
        new_matrix.append(mlist)

    retuen new_matrix
