#!/usr/bin/python3
my_list = [1, 2, 3, 4, 5]
idx = 3
def element_at(my_list, idx):
    for i in range(0,len(my_list)):
        if idx < 0 or idx > len(my_list):
            return None
        return mylist[idx]
