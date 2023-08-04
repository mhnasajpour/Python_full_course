def h(n):
    if n == 0:
        return 6
    if n == 1:
        return -4
    if n == 2:
        return 1
    return 4 * h(n-1) - 2 * h(n-2) + h(n-3)
    
n = int(input())
print(h(n))