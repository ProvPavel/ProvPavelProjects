from sys import stdin

data = stdin.read()
earth_picture = list(map(lambda x: x.rstrip(), data.split('\n')))
my_list = []
for i in range(len(earth_picture)):
    for j in range(len(earth_picture[i])):
        if earth_picture[i][j] == '.':
            flag = True
            for k in range(len(my_list)):
                if [i - 1, j - 1] in my_list[k]:
                    flag = False
                    my_list[k].append([i, j])
                if [i - 1, j] in my_list[k]:
                    flag = False
                    my_list[k].append([i, j])
                if [i - 1, j + 1] in my_list[k]:
                    flag = False
                    my_list[k].append([i, j])
                if [i, j - 1] in my_list[k]:
                    flag = False
                    my_list[k].append([i, j])
                if [i, j + 1] in my_list[k]:
                    flag = False
                    my_list[k].append([i, j])
                if [i + 1, j - 1] in my_list[k]:
                    flag = False
                    my_list[k].append([i, j])
                if [i + 1, j] in my_list[k]:
                    flag = False
                    my_list[k].append([i, j])
                if [i + 1, j + 1] in my_list[k]:
                    flag = False
                    my_list[k].append([i, j])
            if flag:
                my_list.append([[i, j]])
            c = []
            for p in range(len(my_list)):
                if [i, j] in my_list[p]:
                    c.append(p)
            if len(c) == 2:
                my_list[c[0]] = my_list[c[0]] + my_list[c[1]]
                my_list.remove(my_list[c[1]])
print(len(my_list))
