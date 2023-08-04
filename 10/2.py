def is_valid_result(num1, num2):
    if -0.2 <= num1 - num2 <= 0.2:
        return True
    return False

def eq1(x, y): 
    expected_result = x - x // 1
    return is_valid_result(expected_result, y)

def eq2(x, y):
    expected_result = x ** 2 + x
    return is_valid_result(expected_result, y)

def eq3(x, y):
    expected_result = abs(-x ** 3 + 1) + x ** 3
    return is_valid_result(expected_result, y)

count = int(input())
sum1, sum2, sum3 = 0, 0, 0
for _ in range(count):
    x, y = map(float, input().split())
    if eq1(x, y):
        sum1 += 1
    if eq2(x, y):
        sum2 += 1
    if eq3(x, y):
        sum3 += 1

if sum1 == count:
    print(1)
if sum2 == count:
    print(2)
if sum3 == count:
    print(3)
if sum1 != count and sum2 != count and sum3 != count:
    print('No ones')
