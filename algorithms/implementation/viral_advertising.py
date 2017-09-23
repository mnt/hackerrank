import math

n = int(input().strip())

liked = 0
shared = 5
for i in range(0, n):
    liked += math.floor(shared / 2)
    shared = math.floor(shared / 2) * 3

print(liked)
