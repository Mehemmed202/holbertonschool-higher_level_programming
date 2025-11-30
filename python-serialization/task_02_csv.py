#!/usr/bin/python3
"""a"""


import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        data = []

        with open(csv_filename, "r", encoding="UTF-8") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    data.append(row)

        with open("data.json", "w") as f:
            json.dump(data, f)

        return True

    except (FileNotFoundError, Exception):
        return False
