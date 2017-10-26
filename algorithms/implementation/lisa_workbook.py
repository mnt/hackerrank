n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
a = [int(_) for _ in input().strip().split()]

page = 1
s = 0
for questions in a:
    for question in range(1, questions + 1):
        if page == question:
            s += 1

        if question % k == 0:
            page += 1

    if questions % k != 0:
        page += 1

print(s)
