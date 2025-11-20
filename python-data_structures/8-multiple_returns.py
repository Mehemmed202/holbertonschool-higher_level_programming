#!/usr/bin/python3
def multiple_returns(sentence):
    c = 0;
    for i in sentence:
        c = c + 1
    if c > 0:
        first = sentnce[0]
        print("Length: {} - First character: {}".format(c, first))

