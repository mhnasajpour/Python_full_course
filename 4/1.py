n = int(input())
k = int(input())
half = int(n / 2 + 0.5)
print((k * 2 - 1) if k <= half else (k-half) * 2)
