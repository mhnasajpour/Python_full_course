number = int(input())

if number == 1:
    print(2)
    exit()

number_copy = number
sum = 0
while number_copy:
    sum += number_copy % 10
    number_copy //= 10

if number % 2 == 0:
    number -= 1

while sum:
    number += 2
    for i in range(3, number//2 + 1, 2):
        if number % i == 0:
            break
    else:
        sum -= 1

print(number)
