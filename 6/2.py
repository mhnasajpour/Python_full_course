x = int(input())
n = int(input())
i = 1
fact = 1
result = 0
while i < n:
    result += (x**i) / fact
    i += 1
    fact *= i
print(f'{result + 1:.3f}')
