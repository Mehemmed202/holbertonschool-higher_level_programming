#!/usr/bin/python3
"""a"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.openurl(url) as response:
        print(response.headers.get('X-Request-Id'))
