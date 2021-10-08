from random import choice

f = open('test123/lines.txt')
data = f.readlines()
if data:
    print(choice(data))
f.close()
