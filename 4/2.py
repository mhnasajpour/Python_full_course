number = int(input())
print(number // 2)

# print(f'{2 + (number % 2)} {"2 " * (number // 2 - 1)}')
# or

if number % 2:
    print(3, end=' ')
else:
    print(2, end=' ')
print('2 ' * (number // 2 - 1))
