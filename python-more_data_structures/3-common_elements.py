#!/usr/bin/python3
def common_elements(set_1, set_2):
    mylist = []
    for word in set_1:
        if word in set_2:
            mylist.append(word)
    return mylist
