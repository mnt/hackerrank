#!/bin/python3

import sys

def getRecord(s):
    most = 0
    least = 0
    high = s[0]
    low = s[0]
    for i in range(1, len(s)):
        current = s[i]
        if current > high:
            most = most + 1
            high = current
        if current < low:
            least = least + 1
            low = current
    return most, least

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
