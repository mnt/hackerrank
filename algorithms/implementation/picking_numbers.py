#!/bin/python3

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

scores = []
for i in range(0, n):
    score = max(a.count(a[i]) + a.count(a[i] + 1), a.count(a[i]) + a.count(a[i] - 1))
    scores.append(score)

print(max(scores))
