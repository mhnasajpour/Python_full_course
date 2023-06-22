a = float(input())
b = float(input())
c = float(input())

if not a:
    if b:
        print(f'{-c/b :.3f}')
    else:
        print('IMPOSSIBLE')
else:
    delta = b**2-(4*a*c)
    if delta > 0:
        print(f'{(-b-delta**0.5)/(2*a):.3f}')
        print(f'{(-b+delta**0.5)/(2*a):.3f}')
    elif delta == 0:
        if b:
            print(f'{-b/(2*a):.3f}')
        else:
            print(f'{0:.3f}')
    else:
        print('IMPOSSIBLE')
