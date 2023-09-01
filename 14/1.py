def print_result(result):
    if not result:
        print('emptyset')
        return
    result = list(result)
    result.sort()
    for i in result:
        print(i, end=' ')
    print()

u = set(input().split())
a = set(input().split())
b = set(input().split())

print_result(u)
print_result(u.difference(a))
print_result(a.union(b))
print_result(a.intersection(b))
print_result(a.difference(b))