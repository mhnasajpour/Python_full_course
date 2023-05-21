string = input()  # a|b|c
sep1 = string.find('|')
sep2 = string.rfind('|')
a = int(string[:sep1])
b = int(string[sep1+1:sep2])
c = int(string[sep2+1:])

check = bool(a**2 + b**2 - c**2)
print(
    f'Because of {a**2}+{b**2}{"!" * check}={c**2}, the triangle is {"not " * check}right-angled.')
