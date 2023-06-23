number = int(input())
i = 1
while i <= number:
    j = 1
    while j <= number:
        print(i * j, end=' ')
        j += 1
    i += 1
    print()
