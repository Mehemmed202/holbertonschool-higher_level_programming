#!/usr/bin/python3
"""a"""


class Student:
    """a"""


    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        my_dict = self.__dict__
        if isinstance(attrs, list) and all(isinstance(attrs, str) for a in attrs):
            return {k: my_dict[k] for k in attrs if k in my_dict}

        return my_dict
