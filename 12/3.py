def gcd(a, b):
    if a > b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

length, text = int(input()), input()
eq, equation = text.find('='), []

for i in range(eq):
    if i == 0 and text[i] != '-':
        equation.append('+')
    if text[i] == '+' or text[i] == '-':
        equation.append(text[i])
    else:
        equation[-1] += text[i]
for i in range(eq+1, length):
    if i == eq+1 and text[i] != '-':
        equation.append('-')
    if text[i] == '+' or text[i] == '-':
        equation.append('-' if text[i] == '+' else '+')
    else:
        equation[-1] += text[i]

# ax + b = 0
a, b = 0, 0
for segment in equation:
    if segment[-1] == 'x':
        if len(segment) == 2:
            a += int(segment[0]+'1')
        else:
            a += int(segment[:-1])
    else:
        b += int(segment)
        
if a:
    if a < 0 and b > 0:
        print(b // gcd(a, b), -a // gcd(a, b))
    else:
        print(-b // gcd(a, b), a // gcd(a, b))
else:
    print('invalid')