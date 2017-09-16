n = int(input().strip())
s = list(input().strip())

count = 0
level = 0

for step in s:
    level = level + 1 if step == 'U' else level - 1

    if level == 0 and step == 'U':
        count+= 1

print(count)
