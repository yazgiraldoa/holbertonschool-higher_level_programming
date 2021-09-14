#!/usr/bin/python3


def multiple_returns(sentence):
    if len(sentence) == 0:
        info = len(sentence), None
        return info
    else:
        info = len(sentence), sentence[0]
        return info
