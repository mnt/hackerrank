#!/bin/python3

import sys

def solve(n, s, d, m):
    # Complete this function
    count = 0
    for i in range(0, n - m + 1):
        if sum(s[i:i+m]) == d:
            count = count + 1

    return count

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
