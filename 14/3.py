number = int(input())
frames = []

for i in range(number):
    begin, end = map(int, input().split())
    frames.append({i for i in range(begin, end+1)})

begin, end = int(input()), int(input())
period = {i for i in range(begin, end+1)}

for i in range(number):
    period.difference_update(frames[i])

print('true' if len(period) == 0 else 'false')