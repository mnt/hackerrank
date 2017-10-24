q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    balls = {}
    containers = [0] * n
    for c in range(n):
        for i, j in enumerate(input().strip().split(' ')):
            j = int(j)
            if i not in balls:
                balls[i] = 0
            balls[i] += j
            containers[c] += j

    balls = list(balls.values())
    balls.sort()
    containers.sort()

    if balls == containers:
        print("Possible")
    else:
        print("Impossible")
