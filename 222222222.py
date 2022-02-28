from json import load
import requests


def first(string):
    return string[0]


def second(string):
    return string[2]


res = []
flight = open('flight.json', 'r', encoding='utf-8')
a = load(flight)
url = 'http://' + a['address'] + ':' + a['port']
c = requests.get(url).json()
for di in c:
    elem = "name"
    num = "visible_size"
    if int(di[num]) >= int(a['size']):
        res.append([str(di[elem]), str(di[num]), di[num] * a['height'] * a['scale']])
res = sorted(res, key=first)
res = sorted(res, key=second, reverse=True)
res = list(map(lambda x: [x[0], x[1], str(x[2])], res))
b = open('sizes.csv', 'a')
b.write('name:visible_size:real_size\n')
for p in res:
    b.write(':'.join(p) + '\n')
