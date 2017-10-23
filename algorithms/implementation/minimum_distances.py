n = int(input().strip())
arr = [int(_) for _ in input().strip().split(' ')]

distance = -1
for i in range(0, n):
    for j in range(i + 1, n):
        if arr[i] == arr[j] and (j - i < distance or distance == -1):
            distance = j - i

print(distance)
