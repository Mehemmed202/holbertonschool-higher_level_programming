#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    k = []
    for i in range(x):
        try:
            k.append(str(my_list[i]))
        except:
            return (''.join(k))
    return (''.join(k))
