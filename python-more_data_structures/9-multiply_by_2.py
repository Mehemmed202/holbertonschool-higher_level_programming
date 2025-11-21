#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for i in a_dictionary.keys():
        a_dictionary[i] = 2 * a_dictionary[i]
    return a_dictionary
