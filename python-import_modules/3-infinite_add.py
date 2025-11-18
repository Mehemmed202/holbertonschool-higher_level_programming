#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    c = 0
    for i in range(1, len(argv)):
        c = c + int(argv[i])
    print(c)

