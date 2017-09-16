#!/bin/python3
import datetime
import sys

def solve(year):
    if year < 1918:
        feb = 29 if year % 4 == 0  else 28
    elif year > 1918:
        feb = 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28
    else:
        feb = 15

    months = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(0, len(months)):
        if sum(months[0:i+1]) > 256:
            month = i + 1
            day = 256 - sum(months[0:i])
            break

    return "%02d.%02d.%s" % (day, month, year)


year = int(input().strip())
result = solve(year)
print(result)
