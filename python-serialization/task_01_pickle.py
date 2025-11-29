#!/usr/bin/python3
"""a"""


import json
import pickle

class CustomObject:
    """a"""


    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        for k, v in self.__dict__.items():
            i = "{}: {}".format(k, v)
            print(i.capitalize())

    def serialize(self, filename):
        with open(filename, "w", encoding="UTF-8") as f:
            return pickle.dump(self, f)
    
    @classmethod
    def deserialize(cls, filename):
        with open(filename, "r", encoding="UTF-8") as fl:
            data = pickle.load(fl)
        return cls(**data)
