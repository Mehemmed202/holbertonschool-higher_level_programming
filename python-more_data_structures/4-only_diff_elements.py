#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    mylist = []
    for word in set_1:
        if word not in set_2:
            mylist.append(word)
    return mylist
