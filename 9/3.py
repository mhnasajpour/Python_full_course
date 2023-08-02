def factors(number):
    count = 0
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            count += 2
    if i ** 2 == number:
        count -= 1
    return count

a, b, c = map(int, input().split())
n = int(input())
k = int(input())

for x in range(n):
    y = a * x**2 + b * x + c
    if factors(y) >= k:
        print(y)
        break
else:
    print('No match found!')