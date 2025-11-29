#!/usr/bin/python3
"""a"""


import json


def save_to_json_file(my_obj, filename):
    """a"""

    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
