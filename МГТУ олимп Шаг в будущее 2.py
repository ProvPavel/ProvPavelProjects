n = int(input())
data = []
for i in range(n):
    data += [j[0].lower() for j in input().split()]
data.sort()
tup = {}
for k in data:
    if k not in tup.keys():
        tup[k] = 1
    else:
        tup[k] += 1
save = [tup[x] for x in tup.keys()]
minim = 1001
for w in range(len(save)):
    for e in range(w, len(save)):
        f = sum(save[:w:])
        g = sum(save[w:e:])
        h = sum(save[e::])
        m = max(abs(f - g), abs(f - h), abs(g - h))
        if m < minim:
            minim = m
print(minim)
