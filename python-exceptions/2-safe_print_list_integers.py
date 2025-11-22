#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    try:
        for i in range(x):
            c = c + 1
            print("{:d}".format(my_list[i]), end="")
    except (IndexError, TypeError):
        pass
