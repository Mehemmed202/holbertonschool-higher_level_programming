#!/usr/bin/python3
"""a"""


def append_write(filename="", text=""):
    """a"""

    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
