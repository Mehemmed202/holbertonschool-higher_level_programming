#!/usr/bin/python3
""""A"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding="UTF-8") as f:
        print(f.write(text))
