my_list = list(map(lambda x: int(x), input().split()))
last = my_list[-1]
my_list.sort()
a = my_list[-1]
for i in my_list:
    x = i
    if a % x != 0:
        m = 0
        while x % 2 == 0:
            x //= 2
            m += 1
        k = 0
        while x % 3 == 0:
            x //= 3
            k += 1
        e = 0
        while x % 5 == 0:
            x //= 5
            e += 1
        f = 0
        while x % 7 == 0:
            x //= 7
            f += 1
        u = 0
        while x % 11 == 0:
            x //= 11
            u += 1
        g = 0
        while x % 13 == 0:
            x //= 13
            g += 1
        t = 0
        while x % 17 == 0:
            x //= 17
            t += 1
        q = 0
        while x % 19 == 0:
            x //= 19
            q += 1

        while a % 2 ** m != 0:
            a *= 2
        while a % 3 ** k != 0:
            a *= 3
        while a % 5 ** e != 0:
            a *= 5
        while a % 7 ** f != 0:
            a *= 7
        while a % 11 ** u != 0:
            a *= 11
        while a % 13 ** g != 0:
            a *= 13
        while a % 17 ** t != 0:
            a *= 17
        while a % 19 ** q != 0:
            a *= 19
        if a % x != 0:
            a *= x
res = a // last
print(res)
