#!/usr/bin/python3
def uppercase(str):
    word=""
    for c in str:
        if 'a' <= c <= 'z':
            word=word + chr(ord(c)-32)
        else:
            word=word + c
    return word

