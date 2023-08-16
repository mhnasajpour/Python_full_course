def sum_profit_in_days(numbers, begin, end):
    sum = 0
    for i in range(begin, end+1):
        sum += numbers[i]
    return sum

_ = int(input())
numbers = list(map(int, input().split()))

max = 0
for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        sum = sum_profit_in_days(numbers, i, j)
        if sum > max:
            max = sum
print(max)