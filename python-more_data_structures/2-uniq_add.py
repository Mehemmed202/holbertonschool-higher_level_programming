#!/usr/bin/python3
def uniq_add(my_list=[]):
    c = 0
    for i in my_list:
        c = c + i
        my_list.remove(i)
    return c
