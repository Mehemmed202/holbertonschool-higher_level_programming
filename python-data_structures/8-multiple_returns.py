#!/usr/bin/python3
def multiple_returns(sentence):
    c = 0;
    for i in sentence:
        c = c + 1
    if c > 0:
        first = sentence[0]
        return (c, first)
