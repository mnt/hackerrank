g = int(input().strip())

for _ in range(g):
    n = int(input().strip())
    a = list(input().strip())

    d = dict()
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1

    happy = n > 1 or (n == 1 and a[0] == '_')

    if '_' in d:
        for k, v in d.items():
            if v == 1 and k != '_':
                happy = False
                break
    else:
        c = 1
        i = 1
        bug = a[0]

        while i < n:
            if a[i] != bug:
                if a[i - 1] != a[i - 2] or i == n - 1:
                    happy = False
                    break

                bug = a[i]
            i += 1

    if happy:
        print('YES')
    else:
        print('NO')
