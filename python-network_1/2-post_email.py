#!/usr/bin/python3
"""a"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]

    values = {"email": email}

    data = urllib.parse.urlencode(values).encode('utf-8')

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))

