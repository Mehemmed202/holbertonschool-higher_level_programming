#!/usr/bin/python3
"""da"""


class Student:
    """a"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        new_dict = {}
        my_dict = attrs.__dict__

        if isinstance(attrs, list) and all(isinstance(a, str) for a in my_dict):
            for k in attrs:
                if k in my_dict:
                    new_dict[k] = my_dict[k]

        return new_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
