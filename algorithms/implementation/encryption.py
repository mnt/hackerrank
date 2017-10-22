#!/bin/python3

import sys
import math

s = input().strip().split(' ')
s = ''.join(s)
row = math.floor(math.sqrt(len(s)))
column = math.ceil(math.sqrt(len(s)))

while row * column < len(s):
    row += 1

matrix = [['' for x in range(column)] for y in range(row)]
count = 0
for y in range(0, row):
    for x in range(0, column):
        matrix[y][x] = s[count]
        count += 1

        if count == len(s):
            break
encrypted = []
for x in range(0, column):
    s = ''
    for y in range(0, row):
        s += matrix[y][x]

    encrypted.append(s)

encrypted = ' '.join(encrypted)
print(encrypted)
