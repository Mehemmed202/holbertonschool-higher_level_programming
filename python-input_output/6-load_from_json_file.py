#!/usr/bin/python3
"""a"""


import json


def load_from_json_file(filename):
    """a"""

    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
