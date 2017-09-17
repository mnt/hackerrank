#!/bin/python3

import sys
from itertools import permutations

s = []
for s_i in range(3):
   for s_temp in input().strip().split(' '):
       s.append(int(s_temp))

magic_squares = []
squares = permutations([1, 2, 3, 4, 5, 6, 7, 8, 9])

for square in squares:
    if (square[0] + square[1] + square[2] == 15 and
    square[3] + square[4] + square[5] == 15 and
    square[6] + square[7] + square[8] == 15 and
    square[0] + square[3] + square[6] == 15 and
    square[1] + square[4] + square[7] == 15 and
    square[2] + square[5] + square[8] == 15 and
    square[0] + square[4] + square[8] == 15 and
    square[2] + square[4] + square[6] == 15):
        magic_squares.append(square)

if tuple(s) in magic_squares:
    print(0)
else:
    cost = 81
    for magic_square in magic_squares:
        temp_cost = 0
        for idx, value in enumerate(s):
            temp_cost += abs(magic_square[idx] - value)

        if (temp_cost < cost):
            cost = temp_cost

    print(cost)
