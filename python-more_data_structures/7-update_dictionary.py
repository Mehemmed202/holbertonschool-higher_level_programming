#!/usr/bin/python3
a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
def update_dictionary(a_dictionary, key, value):
    a_dictionary.update({key : value})
    for i in a_dictionary.keys():
        print("{}: {}".format(key, a_dictionary[key]))
