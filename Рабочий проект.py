from random import choice

f = open('test123/lines.txt')
for number, line in enumerate(f):
    a = choice([0, 1])
    if a:
        print(line)
        break
f.close()
