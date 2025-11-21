#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dictionary = []
    for i in a_dictionary.keys():
        n_dictionary[int(i)] = 2 * a_dictionary[int(i)]
    return n_dictionary
