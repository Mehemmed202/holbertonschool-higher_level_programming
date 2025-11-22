#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    k = []
    c = 0
    try:
        for i in range(x):
            c = c + 1
            k.append(mylist[i])
            print("{:d}".format("".join(k)))
    except (IndexError, TypeError):


