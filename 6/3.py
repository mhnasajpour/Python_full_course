questions = int(input())
while questions:
    number = input()
    max_iters = len(number) * 9
    number = int(number)
    sum_of_digits = 1
    while max_iters:
        number -= 1
        sum = 0
        temp_number = number
        while sum <= sum_of_digits and temp_number:
            sum += temp_number % 10
            temp_number = temp_number // 10
        if sum_of_digits == sum:
            print('Yes')
            break
        sum_of_digits += 1
        max_iters -= 1
    else:
        print('No')
    questions -= 1
