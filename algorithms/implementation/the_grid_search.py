t = int(input().strip())

for a0 in range(t):
    R, C = [int(_) for _ in input().strip().split(' ')]
    g = []
    p = []
    for _ in range(R):
        g.append(list(input().strip()))

    r, c = [int(_) for _ in input().strip().split(' ')]
    for _ in range(r):
        p.append(list(input().strip()))

    found = False
    for i in range(R):
        for j in range(C):
            if g[i][j] == p[0][0] and i + r - 1 < R and j + c - 1 < C:
                found = True
                for y in range(r):
                    for x in range(c):
                        if p[y][x] != g[i + y][j + x]:
                            found = False

                        if not found:
                            break
                    if not found:
                        break
            if found:
                break
        if found:
            break

    if found:
        print('YES')
    else:
        print('NO')
