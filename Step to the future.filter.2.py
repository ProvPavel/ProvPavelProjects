y = input().split()
p = float(y[0])
n = int(y[1])
result = '0.'
for i in range(n):
    if p >= 0.75:
        result += '3'
        p -= 0.75
        p *= 4
    elif p >= 0.5:
        result += '2'
        p -= 0.5
        p *= 4
    elif p >= 0.25:
        result += '1'
        p -= 0.25
        p *= 4
    else:
        result += '0'
        p *= 4
print(float(result)) if len(result) < n + 2 else print(result)
