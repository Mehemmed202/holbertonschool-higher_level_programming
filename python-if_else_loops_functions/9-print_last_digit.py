#!/usr/bin/python3
def print_last_digit(number):
    for char in str:
        ascii_val = ord(char)
        if ascii_val >= 97 and ascii_val <= 122:
            char_to_print = chr(ascii_val - 32)
        else:
            char_to_print = char
        print("{}".format(char_to_print), end="")
    print("{}".format(""))
