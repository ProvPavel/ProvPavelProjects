data = open('trophies.csv', 'r')
b = [i.rstrip().split('.') for i in data.readlines()]
s = input()
h = int(input())
res = set()
for j in b:
    try:
        if j[1] == s and int(j[2]) >= h:
            res.add(j[0])
    except Exception:
        continue
print(*res, sep='\n')
