def nums_right_side_their_square(m, n):
    for i in range(m+1, n):
        if str(i**2).endswith(str(i)):
            print(i, end=' ')
    print()

def sum_digits(number):
    sum = 0
    while number:
        sum += number % 10
        number //= 10
    return sum
        

def sum_digits_of_primes(m, n):
    sum = 0
    for number in range(m+1, n):
        for i in range(2, number//2 + 1):
            if number % i == 0:
                break
        else:
            sum += sum_digits(number)
    print(sum)

m = int(input())
n = int(input())

if (m + n) % 2 == 0:
    nums_right_side_their_square(m, n)
else:
    sum_digits_of_primes(m, n)