#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    mylist = []
    (set_1).extend(set_2)
    for word in set_1:
        if (set_1).count(word) == 1:
            mylist.append(word)
    return mylist
