import sys

v = []
for line in sys.stdin.readlines():
    v.append(line.rstrip())
strings = list(map(lambda x: list(map(lambda y: int(y), x.split(' '))), v))
elements = []
for j in range(len(strings[0])):
    a = []
    for h in range(len(strings)):
        a.append(strings[h][j])
    elements.append(a)
sum_strings = list(map(lambda x: sum(x), strings))
sum_elements = list(map(lambda x: sum(x), elements))
s, string_index, element_index = -1, 0, 0
for i in sum_strings:
    if i in sum_elements and i > s:
        s, string_index, element_index = i, sum_strings.index(i), sum_elements.index(i)
if s == -1:
    print('NO')
else:
    string = strings[string_index]
    strings[string_index] = elements[element_index]
    for m in range(len(strings)):
        for o in range(len(strings[m])):
            if o == element_index:
                strings[m][o] = string[m]
    for _ in strings:
        print(*_)
