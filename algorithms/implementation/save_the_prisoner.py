#!/bin/python3

import sys

def saveThePrisoner(n, m, s):
    remainder = (m - 1) % n
    if remainder + s <= n:
        return remainder + s
    else:
        return (remainder + s) - n


t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)
