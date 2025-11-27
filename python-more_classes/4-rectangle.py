#!/usr/bin/python3
"""a"""


class Rectangle:
    """s"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)
        return perimeter

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            print()
        else:
            for i in (self.__height):
                print(self.__width * "#")
                if i != self.__height - 1:
                    print()
                else:
                    print("")

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
