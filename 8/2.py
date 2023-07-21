number = int(input())
i = 2
flag = False

while number > 1:
    counter = 0
    while number % i == 0:
        counter += 1
        number //= i
    if counter:
        print(f'{"*" if flag == True else ""}{i}{"^" if counter > 1 else""}{counter if counter > 1 else ""}', end='')
        flag = True
    i += 1    