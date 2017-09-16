#!/bin/python3

import sys
import math

def sockMerchant(n, ar):
    socks = {}

    for i in ar:
        if i in socks:
            socks[i] += 1
        else:
            socks[i] = 1

    count = 0
    for k, v in socks.items():
        count += math.floor(v / 2)

    return count

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
