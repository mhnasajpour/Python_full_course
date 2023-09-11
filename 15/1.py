text = input()
result = ''

i, start_char = 1, 0
for i in range(1, len(text)+1):
    if i == len(text) or text[i] != text[i-1]:
        result += f'{text[i-1]}{i - start_char}'
        start_char = i

print(result)