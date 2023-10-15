n = int(input())
absolute = {}
initial = {}
request = {}
current = {}
for i in range(n):
    q = input().split()
    absolute[q[0]] = [int(q[1]), int(q[2])]
    initial[q[0]] = [int(q[1]), int(q[2])]
    current[q[0]] = 0
m = int(input())

for j in range(m):
    w = input().split()
    change_min = 0
    change_max = 0
    request[w[0]] = w[2]
    if w[2] in request.keys():
        if '+' in w:
            if absolute[w[2]][1] + int(w[4]) > absolute[w[0]][1]:
                initial[w[2]][1] -= (absolute[w[2]][1] + int(w[4]) - absolute[w[0]][1]) + current[w[0]]
                change_max = -(absolute[w[2]][1] + int(w[4]) - absolute[w[0]][1])
            if absolute[w[2]][0] + int(w[4]) < absolute[w[0]][0]:
                initial[w[2]][0] += (absolute[w[0]][0] - (absolute[w[2]][0] + int(w[4]))) - current[w[0]]
                change_min = (absolute[w[0]][0] - (absolute[w[2]][0] + int(w[4])))
            current[w[0]] += int(w[4])
        else:
            if absolute[w[2]][0] - int(w[4]) < absolute[w[0]][0]:
                initial[w[2]][0] += (absolute[w[0]][0] - (absolute[w[2]][0] - int(w[4]))) - current[w[2]]
                change_min = (absolute[w[0]][0] - (absolute[w[2]][0] - int(w[4])))
            if absolute[w[2]][1] - int(w[4]) > absolute[w[0]][1]:
                initial[w[2]][1] -= (absolute[w[2]][1] - int(w[4]) - absolute[w[0]][1]) + current[w[0]]
                change_max = -(absolute[w[2]][1] - int(w[4]) - absolute[w[0]][1])
            current[w[0]] -= int(w[4])
        if w[2] in request.keys():
            initial[request[w[2]]][0] += change_min
            initial[request[w[2]]][1] += change_max
        if change_min != 0:
            initial[w[2]][0] -= initial[request[w[2]]][0]
        if change_max != 0:
            initial[w[2]][1] += initial[request[w[2]]][1]
    else:
        if '+' in w:
            if absolute[w[2]][1] + int(w[4]) > absolute[w[0]][1]:
                initial[w[2]][1] -= (absolute[w[2]][1] + int(w[4]) - absolute[w[0]][1]) + current[w[0]]
                change_max = -(absolute[w[2]][1] + int(w[4]) - absolute[w[0]][1])
            if absolute[w[2]][0] + int(w[4]) < absolute[w[0]][0]:
                initial[w[2]][0] += (absolute[w[0]][0] - (absolute[w[2]][0] + int(w[4]))) - current[w[0]]
                change_min = (absolute[w[0]][0] - (absolute[w[2]][0] + int(w[4])))
            current[w[0]] += int(w[4])
        else:
            if absolute[w[2]][0] - int(w[4]) < absolute[w[0]][0]:
                initial[w[2]][0] += (absolute[w[0]][0] - (absolute[w[2]][0] - int(w[4]))) - current[w[2]]
                change_min = (absolute[w[0]][0] - (absolute[w[2]][0] - int(w[4])))
            if absolute[w[2]][1] - int(w[4]) > absolute[w[0]][1]:
                initial[w[2]][1] -= (absolute[w[2]][1] - int(w[4]) - absolute[w[0]][1]) + current[w[0]]
for k in sorted(initial.keys()):
    print(k, *initial[k])
