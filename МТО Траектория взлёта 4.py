A, B, C, D = list(map(lambda x: int(x), input().split()))
n = int(input())
list_of_results = []
for i in range(n):
    res = []
    a, b, c, d = list(map(lambda x: int(x), input().split()))
    for j in range(c - a + 1):
        string = []
        str_input = input()
        for k in range(d - b + 1):
            if B - b <= k <= D - b:
                string.append(str_input[k])
        if A - a <= j <= C - a:
            res.append(string)
    list_of_results.append(res)
flag = True
for q in list_of_results:
    for w in list_of_results:
        if q != w:
            flag = False
if flag:
    for r in list_of_results[0]:
        print(''.join(r))
else:
    print('Check photos')
