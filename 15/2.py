def sum(num1, num2):
    result = ''
    for i in range(3):
        result += str((int(num1[i]) + int(num2[i])) % 10)

    return int(result)


list1 = input().split()
list2 = input().split()
list1_transformed, list2_transformed = [], []

for i in range(5):
    list1_transformed.append([list1[i], list1[(i + 1) % 5], list1[(i + 2) % 5]])
    list2_transformed.append([list2[i], list2[(i + 1) % 5], list2[(i + 2) % 5]])

for i in range(5):
    for j in range(5):
        if sum(list1_transformed[i], list2_transformed[j]) % 6 == 0:
            print("Boro joloo :)")
            exit()

print("Gir oftadi :(")
