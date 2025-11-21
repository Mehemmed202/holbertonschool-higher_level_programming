#!/usr/bin/python3
def best_score(a_dictionary):
    k = 0
    for i in a_dictionary.keys():
        if a_dictionary[i] > k:
            k = a_dictionary[i]
    return k
