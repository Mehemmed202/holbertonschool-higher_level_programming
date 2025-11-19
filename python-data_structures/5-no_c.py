#!/usr/bin/python3
new_string = ""
def no_c(my_string):
    for i in my_string:
        if i != "c" or i != "C":
            new_string.append(i)
    return new_string
