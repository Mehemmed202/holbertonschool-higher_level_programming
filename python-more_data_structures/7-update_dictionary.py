#!/usr/bin/python3
a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
def update_dictionary(a_dictionary, key, value):
    a_dictionary.update({key : value})
    dct = a_dictionary.keys()
    for i in dct:
        print("{}: {}".format(key, a_dictionary[key]))
