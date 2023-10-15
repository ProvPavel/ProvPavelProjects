from PIL import Image
im = Image.open('image.png')

pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
earth_picture = []
for t in pixels:
    earth_picture.append(list(map(lambda x: 'X' if x == (0, 0, 0) else '.', t)))
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
