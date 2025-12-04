#!/usr/bin/python3
"""a"""

import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(response.status_code)
    print(response.json())
