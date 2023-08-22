line1, line2, line3 = input(), input(), input()
line1 = [line1[i:i+5] for i in range(0, len(line1), 5)]
line2 = [line2[i:i+5] for i in range(0, len(line2), 5)]
for column, i in enumerate(line1):
	if i == '*****':
		print('T', end='')
	elif i == 'oo*oo':
		print('A', end='')
	elif i == '**o**':
		print('M', end='')
	elif i == '*ooo*':
		if line2[column][0] == 'o':
			print('X', end='')
		else:
			print('N', end='')