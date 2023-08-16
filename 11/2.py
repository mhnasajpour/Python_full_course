numbers = input().split()
number_of_queries = int(input())

for _ in range(number_of_queries):
    query, value = input().split()
    if query == 'add':
        if value in numbers:
            print('exist')
        else:
            numbers.append(value)
    elif query == 'del':
        if value not in numbers:
            print('not exist')
        else:
            numbers.remove(value)

for i in numbers:
    print(i)