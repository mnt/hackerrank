#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    count = 0
    n = int(input().strip())
    digits = str(n)
    for d in digits:
        d = int(d)
        if d != 0 and n % d == 0:
            count += 1

    print(count)
