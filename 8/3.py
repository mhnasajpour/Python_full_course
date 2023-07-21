number = int(input())

if number == 1:
    print('#')
    exit()

print('#' * number)
for i in range(1, number // 2):
    print('#', end='')
    print(' ' * (i - 1), end='')
    print('#', end='')
    print(' ' * (number - 2 * (i + 1)), end='')
    print('#' * (i + 1), end='')
    print()
print('#' + ' ' * (number // 2 - 1) + '#' * (number // 2 + 1))
for i in range(1, number // 2):
    print('#', end='')
    print(' ' * (number // 2 - i - 1), end='')
    print('#', end='')
    print(' ' * (2 * i - 1), end='')
    print('#' * (number // 2 - i + 1), end='')
    print()
print('#' * number)
