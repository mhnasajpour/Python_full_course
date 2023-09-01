def diff_times(time1, time2):
    # time1 should be lower than or equal time2
    # time format => (xx:xx)
    if time1[:2] == time2[:2]:
        return int(time2[3:]) - int(time1[3:])
    else: 
        return (int(time2[:2]) - int(time1[:2]) - 1) * 60 + int(time2[3:]) + (60 - int(time1[3:]))
    

number = int(input())
info = {}

for i in range(number):
    name, time = input().split()
    if name in info.keys():
        print(diff_times(info[name], time))
    else:
        info[name] = time
