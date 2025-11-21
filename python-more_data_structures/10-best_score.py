#!/usr/bin/python3
def best_score(a_dictionary):
    k = 0
    c = 0
    for i in a_dictionary.keys():
        if a_dictionary[i] > k:
            c = c + 1
            k = a_dictionary[i]
        if c == 0:
            return None
    for j in a_dictionary:
        if k == a_dictionary[j]:
            return j
