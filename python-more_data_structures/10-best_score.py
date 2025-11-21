#!/usr/bin/python3
def best_score(a_dictionary):
    k = 0
    if not a_dictionary:
        return None
    for i in a_dictionary.keys():
        if a_dictionary[i] > k:
            k = a_dictionary[i]
    for j in a_dictionary:
        if k == a_dictionary[j]:
            return j
