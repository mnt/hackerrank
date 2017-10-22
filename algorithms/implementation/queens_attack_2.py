#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
rQueen,cQueen = input().strip().split(' ')
rQueen,cQueen = [int(rQueen) - 1, int(cQueen) - 1]
obstacles = {}
for a0 in range(k):
    rObstacle,cObstacle = input().strip().split(' ')
    rObstacle,cObstacle = [int(rObstacle) - 1, int(cObstacle) - 1]
    # your code goes here
    obstacles[(cObstacle, rObstacle)] = 1

count = 0

west = (cQueen - 1, rQueen)
north_west = (cQueen - 1, rQueen + 1)
north = (cQueen, rQueen + 1)
north_east = (cQueen + 1, rQueen + 1)
east = (cQueen + 1, rQueen)
south_east = (cQueen + 1, rQueen - 1)
south = (cQueen, rQueen - 1)
south_west = (cQueen - 1, rQueen - 1)

i = 0
while west[0] - i > -1 and (west[0] - i, west[1]) not in obstacles:
    i += 1
    count += 1

i = 0
while north_west[0] - i > -1 and north_west[1] + i < n and (north_west[0] - i, north_west[1] + i) not in obstacles:
    i += 1
    count += 1

i = 0
while north[1] + i < n and (north[0], north[1] + i) not in obstacles:
    i += 1
    count += 1

i = 0
while north_east[0] + i < n and north_east[1] + i < n and (north_east[0] + i, north_east[1] + i) not in obstacles:
    i += 1
    count += 1

i = 0
while east[0] + i < n and (east[0] + i, east[1]) not in obstacles:
    i += 1
    count += 1

i = 0
while south_east[0] + i < n and south_east[1] - i > -1 and (south_east[0] + i, south_east[1] - i) not in obstacles:
    i += 1
    count += 1

i = 0
while south[1] - i > -1 and (south[0], south[1] - i) not in obstacles:
    i += 1
    count += 1

i = 0
while south_west[0] - i > -1 and south_west[1] - i > -1 and (south_west[0] - i, south_west[1] - i) not in obstacles:
    i += 1
    count += 1

print(count)
