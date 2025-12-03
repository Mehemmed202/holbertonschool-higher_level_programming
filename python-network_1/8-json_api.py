#!/usr/bin/python3
"""a"""

import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if sys.argv[1] > 1:
        key = sys.argv[1]
    else:
        key = ""

    payload = {"q": key}
    response = requests.post(url, json=payload)

    try:
        json_response  =response.json()

        if json_response:
            print("[{}] {}".format(json_response.get('id'),
                                   json_response.get('name')))
        else:
            print("No result")
        
    except ValueError:
        print("Not a valid JSON")


