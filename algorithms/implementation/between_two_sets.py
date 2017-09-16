#!/bin/python3

import sys

def getTotalX(a, b):
    # we arrange a and b in order
    a.sort()
    b.sort()

    min = a[-1]
    max = b[0]
    count = 0

    for i in range(min, max + 1):
        isBetween = True
        for factor in a:
            for number in b:
                if i % factor != 0:
                    isBetween = False
                    break
                if number % i != 0:
                    isBetween = False
                    break
        if isBetween == True:
            count = count + 1

    return count

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
