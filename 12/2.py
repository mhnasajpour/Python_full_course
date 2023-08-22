number = int(input())
colors_set = ''
sizes_set = []
for i in range(number):
    size, color = input().split()
    if color not in colors_set:
        colors_set += color
        sizes_set.append([int(size)])
    else:
        sizes_set[colors_set.find(color)].append(int(size))

for i in range(len(sizes_set)):
    sizes_set[i].sort(reverse=True)
    for size in sizes_set[i]:
        print(size, colors_set[i])
