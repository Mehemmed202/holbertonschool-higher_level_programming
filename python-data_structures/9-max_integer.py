#!/usr/bin/python3
def max_integer(my_list=[]):
    h = int(my_list[0])
    for i in my_list:
        if int(i) > h:
            h = int(i)
    return h
