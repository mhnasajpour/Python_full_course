number = input()

num1 = int(number[0])
num2 = int(number[1])
num3 = int(number[2])
num4 = int(number[3])

min = 9
max = 0

if num1 < min:
    min = num1
if num1 > max:
    max = num1
if num2 < min:
    min = num2
if num2 > max:
    max = num2
if num3 < min:
    min = num3
if num3 > max:
    max = num3
if num4 < min:
    min = num4
if num4 > max:
    max = num4
print(f'{max}*{min}')
