number = int(input())
n = 0
while number >= 2 ** n:
    n += 1
print(f'{(number - (2 ** (n - 1))) * 2 + 1}')