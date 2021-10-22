name_1 = input()
name_2 = input()
file_1 = open(name_1, 'r')
file_2 = open(name_2, 'r')
result = open('regards.txt', 'a')
file_1_list = list(map(lambda x: x.strip().split(), file_1.readlines()))
file_2_list = list(map(lambda x: x.strip().split(), file_2.readlines()))
color = input()
numbers = 0
for i in file_1_list:
    if color == i[1]:
        color_number = i[0]
        numbers = file_2_list[int(color_number) - 1]
if numbers == 0:
    result.write('Error')
else:
    colors = set()
    for j in file_1_list:
        if j[0] in numbers:
            colors.add(j[1])
    for c in colors:
        result.write(c)
        result.write('\n')
