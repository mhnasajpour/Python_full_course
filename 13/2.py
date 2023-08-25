def is_mirror(text):
    for i in range(1, len(text)-1):
        if text[i-1] == text[i+1]:
            return True
    return False

def is_frequent(text):
    for i in range(len(text)-3):
        if text.count(text[i]) >= 4:
            return True
    return False

number = int(input())

for i in range(number):
    phone_number = input()
    rond = is_mirror(phone_number) + is_frequent(phone_number)
    print('notrond' if rond == 0 else 'rond' if rond == 1 else 'superrond')