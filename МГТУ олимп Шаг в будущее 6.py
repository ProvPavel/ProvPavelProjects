n = int(input())
absolute = {}
initial = {}
for i in range(n):
    q = input().split()
    absolute[q[0]] = [int(q[1]), int(q[2])]
    initial[q[0]] = [int(q[1]), int(q[2])]
m = int(input())
data = []
for i in range(m):
    data.append(input())
data.reverse()
for i in range(m):
    for j in range(i + 1, m):
        if data[i][4] == data[j][0]:
            data[i] = data[i][:4:] + data[j][4::] + data[i][5::]
for i in data:
    w = i.split()
    s = w[3::]
    a = []
    for j in range(0, len(s) // 2, 2):
        a.append(int(s[j] + s[j + 1]))
    p = sum(a)
    w = w[:3:]
    if p > 0:
        if absolute[w[2]][1] + p > absolute[w[0]][1]:
            initial[w[2]][1] -= (absolute[w[2]][1] + p - absolute[w[0]][1])
        if absolute[w[2]][0] - p < absolute[w[0]][0]:
            initial[w[2]][0] += (absolute[w[0]][0] - (absolute[w[2]][0] + p))
    else:
        if absolute[w[2]][0] + p < absolute[w[0]][0]:
            initial[w[2]][0] += (absolute[w[0]][0] - (absolute[w[2]][0] - p))
        if absolute[w[2]][1] - p > absolute[w[0]][1]:
            initial[w[2]][1] -= (absolute[w[2]][1] - p - absolute[w[0]][1])
for k in sorted(initial.keys()):
    print(k, *initial[k])
