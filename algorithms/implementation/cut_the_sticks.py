#!/bin/python3

import sys
import math

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

arr.sort()

while len(arr) != 0:
    print(len(arr))
    smallest = arr[0]
    arr = list(map(lambda x: x - smallest, arr))
    arr = [y for y in arr if y > 0]
