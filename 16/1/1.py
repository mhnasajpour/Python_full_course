def get_content_of_file(file_path):
    file = open(file_path)
    list_of_contents = file.readlines()
    file.close()
    return list_of_contents

file1 = get_content_of_file('1_file1.txt')
file2 = get_content_of_file('1_file2.txt')

result_file = open('1_file3.txt', 'w')
for i in range(len(file1)):
    if file1[i] == file2[i]:
        result_file.write(file1[i])
result_file.close()