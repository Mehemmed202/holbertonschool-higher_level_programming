#!/usr/bin/python3
"""a"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a"""

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        print("[Square] {}/{}")
