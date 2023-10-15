n = input()
count = 0
for i in range(len(n) - 1):
    if int(n[i:i + 2]) % 3 == 0:
        count += 1
print(count)
