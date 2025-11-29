#!/usr/bin/python3
"""a"""


import json


def load_from_json_file(filename):
    """a"""

    with open(filename, "w", encoding="UTF-8") as f:
        json.load(f)
