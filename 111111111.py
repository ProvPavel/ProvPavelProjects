from json import dump
from sys import stdin

a = {'beings': {},
     'nature': {},
     'rest': {}}
data = stdin.readlines()
for i in data:
    x = i.rstrip().split(': ')
    if x[0] == '1':
        if len(x[1].split()) not in a['beings']:
            a['beings'][len(x[1].split())] = []
        a['beings'][len(x[1].split())].append(x[1].split()[-1])
        a['beings'][len(x[1].split())].sort(reverse=True)
    elif x[0] == '2':
        if len(x[1].split()) not in a['nature']:
            a['nature'][len(x[1].split())] = []
        a['nature'][len(x[1].split())].append(x[1].split()[-1])
        a['nature'][len(x[1].split())].sort(reverse=True)
    elif x[0] == '3':
        if len(x[1].split()) not in a['rest']:
            a['rest'][len(x[1].split())] = []
        a['rest'][len(x[1].split())].append(x[1].split()[-1])
        a['rest'][len(x[1].split())].sort(reverse=True)
b = open('questions.json', 'w')
dump(a, b, indent=4)
