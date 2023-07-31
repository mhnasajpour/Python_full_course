def sum_prime_factors(number):
    sum = 0
    factor = 2
    while number > 1:
        sum += factor if number % factor == 0 else 0
        while number % factor == 0:
            number //= factor 
        factor += 1
    return sum

def sum_digits(number):
    sum = 0
    while number:
        sum += number % 10
        number //= 10
    return sum

def has_parent(number):
    for i in range(number - 1, 0, -1):
        if sum_prime_factors(i) + sum_digits(i) + i == number:
            return 'Yes'
    return 'No'

count = int(input())
for _ in range(count):
    number = int(input())
    print(has_parent(number))