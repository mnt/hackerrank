#!/bin/python3

import sys


n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
# your code goes here
scores = list(set(scores))
scores.sort(reverse=True)
index = 0
rank = len(scores) - 1

for i in range(0, m):
    for j in range(rank, -1, -1):
        if alice[i] >= scores[j] and (j == 0 or alice[i] < scores[j - 1]):
            print(j + 1)
            break
        elif alice[i] < scores[j] and j == len(scores) - 1:
            print(len(scores) + 1)
            break

        rank = j
