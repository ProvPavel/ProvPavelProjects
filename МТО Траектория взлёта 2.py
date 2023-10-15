t = 50
x = 2
y = 3
for i in range(t):
    x, y = x + y, x - y
res = ((x - 2) ** 2 + (y - 3) ** 2) ** 0.5
print(res)
