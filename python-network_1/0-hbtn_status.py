#!/usr/bin/python3
#comment

import urllib.request

if __name__ ==" __main__":
    url="https://intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as f:
        raw_data = f.read()
        data = raw_data.decode("utf-8")
        print("Body response:")
        print(f"\t- type: {type(raw_data)}")
        print(f"\t- content: {raw_data}")
        print(f"\t- utf8 content: {data}")
