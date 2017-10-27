n = int(input().strip())

cavity_map = []
for i in range(n):
    cavity_map.append(list(input().strip()))

for i in range(n):
    for j in range(n):
        cell = int(cavity_map[i][j])

        if i != 0 and j != 0 and i != n - 1 and j != n - 1:
            if (cavity_map[i-1][j] != 'X' and int(cavity_map[i-1][j]) < cell and
            cavity_map[i+1][j] != 'X' and int(cavity_map[i+1][j]) < cell and
            cavity_map[i][j-1] != 'X' and int(cavity_map[i][j-1]) < cell and
            cavity_map[i][j+1] != 'X' and int(cavity_map[i][j+1]) < cell):
                cavity_map[i][j] = "X"

    print(''.join(cavity_map[i]))
