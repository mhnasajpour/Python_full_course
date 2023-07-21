n = int(input()) - 1

if n == 0:
    print(2)

number = 3
digits = 1
while n:
    for i in range(digits-1, -1, -1):
        num = number // (10 ** i)
        if num == 1 or (num > 2 and num % 2 == 0):
            break
        for k in range(3, num // 2):
            if num % k == 0:
                break
        else:
            continue
        break
    else:
        n -= 1
        if not n:
            print(number)

    number += 2
    str_number = str(number)[:-1]
    while str_number and str_number[0] == '1' or '0' in str_number or '2' in str_number[1:] or '4' in str_number or '6' in str_number or '8' in str_number:
        number += 10
        str_number = str(number)[:-1]
    digits = len(str_number) + 1