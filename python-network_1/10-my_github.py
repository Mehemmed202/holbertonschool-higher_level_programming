#!/usr/bin/python3
"""a"""

import sys
import requests

if __name__ == "__main__":
    url = "https://www.github.com/user"
    user = sys.argv[1]
    paswd = sys.argv[2]
    response = requests.get(url, auth=(user, paswd))
    print(response.json().get('id'))
