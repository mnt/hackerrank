#!/bin/python3

import sys
import math

def solve(grades):
    rounded_grades = []
    for grade in grades:
        if grade > 35 and math.ceil(grade / 5) * 5 - grade < 3:
            grade = math.ceil(grade / 5) * 5

        rounded_grades.append(grade)
    return rounded_grades

n = int(input().strip())
grades = []
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)

result = solve(grades)
print ("\n".join(map(str, result)))
