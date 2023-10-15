n = float(input())
a = ''
x = 7
while n > 1:
    a += str(int(n // 5 ** x))
    n %= 5 ** x
    x -= 1
a += '.'
while x > -9:
    a += str(int(n // 5 ** x))
    n %= 5 ** x
    x -= 1
a = float(a)
a = str(a)
a = a.split('.')
print(abs(len(a[0]) - len(a[1])))
