#!/usr/bin/python3
"""a"""

import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(url.status_code)
    print(url.json())
