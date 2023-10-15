data = list(map(lambda x: int(x), open('input.txt', 'r').readline().split()))
count = 0
max_sum = -30001
for i in range(len(data) - 2):
    a = data[i]
    b = data[i + 1]
    c = data[i + 2]
    if (a + b + c) % 3 == 0:
        f = 0
        if a != 0 and b ** 2 - 4 * a * c > 0:
            f = 1
        elif a != 0 and c ** 2 - 4 * a * b > 0:
            f = 1
        elif b != 0 and a ** 2 - 4 * b * c > 0:
            f = 1
        elif b != 0 and c ** 2 - 4 * a * b > 0:
            f = 1
        elif c != 0 and a ** 2 - 4 * b * c > 0:
            f = 1
        elif c != 0 and b ** 2 - 4 * a * c > 0:
            f = 1
        if f:
            count += 1
            max_sum = max(a + b + c, max_sum)
print(count, max_sum)
