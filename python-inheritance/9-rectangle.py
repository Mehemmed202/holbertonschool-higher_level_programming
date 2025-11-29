#!/usr/bin/python3
"""a"""


BaseGeometry = __iport__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """a"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    print("[Rectangle] {}/{}".format(self.__width, self.__height))
