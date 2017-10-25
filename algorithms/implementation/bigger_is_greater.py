n = int(input().strip())

for _ in range(0, n):
    chars = [ord(x) for x in list(input().strip())]
    left = -1
    right = 101

    for i in range(len(chars) - 1, -1, -1):
        found = False
        for j in range(i + 1, len(chars)):
            if chars[j] > chars[i] and (left == -1 or chars[right] > chars[j]):
                left = i
                right = j
                found = True
        if found:
            break

    if left != -1:
        chars[left], chars[right] = chars[right], chars[left]

        lexi_string = chars[left + 1:len(chars)]
        lexi_string.sort()
        rearranged_string = chars[0:left + 1] + lexi_string
        rearranged_string = [chr(x) for x in rearranged_string]
        print(''.join(rearranged_string))
    else:
        print('no answer')
