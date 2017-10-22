generate = True
squares = []
i = 1
while generate:
    square = i * i
    if square <= 10e9:
        squares.append(square)
        i += 1
    else:
        generate = False
        break

n = int(input().strip())
for a0 in range(0, n):
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    count = 0
    for square in squares:
        if square >= a and square <= b:
            count += 1

    print(count)
