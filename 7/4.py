number = int(input())

for row in range(number // 2 + 1):
    print(end=' ' * (number // 2 - row))
    print(end='*' * (row * 2 + 1))
    print(end=' ' * (number // 2 - row) * 2)
    print(end='*' * (row * 2 + 1))
    print(end=' ' * (number // 2 - row))
    print()

for row in range(1, number//2 + 1):
    print(end=' ' * (row))
    print(end='*' * (number - (row * 2)))
    print(end=' ' * (row * 2))
    print(end='*' * (number - (row * 2)))
    print(end=' ' * (row))
    print()
