#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    count = 0
    cancelled = True
    for i in range(0, n):
        if a[i] <= 0:
            count += 1
        if count >= k:
            cancelled = False
            break

    print('YES') if cancelled else print('NO')
