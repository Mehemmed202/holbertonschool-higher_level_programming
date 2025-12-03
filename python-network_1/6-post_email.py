#!/usr/bin/python3
"""a"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {"email": email}

    response = request.post(url, json=payload)
    print("Your email is: {}".format(response.text))
