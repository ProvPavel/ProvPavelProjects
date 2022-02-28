import argparse
import requests
import json

parser = argparse.ArgumentParser()
parser.add_argument('data', nargs='+', type=str)
parser.add_argument('--abc', type=str, default='a')
parser.add_argument('--length', type=int, default=0)

args = parser.parse_args()
server = 'http://' + args.data[0] + ':' + args.data[1]
sources = args.data[2:]

all = requests.request('GET', server).json()
results = []
for i in all:
    if args.abc < i[0]:
        results.append({})
        j = map(lambda x: len(x), all[i])
        res = []
        for k in j:
            if k > args.length:
                res.append(k)
        results[-1]['object'] = i
        results[-1]['min_length'] = min(res)
        results[-1]['max_length'] = max(res)
        results[-1]['average'] = round(sum(res) / len(res))
    elif args.abc not in sources:
        results.append({})
        j = map(lambda x: len(x), all[i])
        res = []
        for k in j:
            res.append(k)
        results[-1]['object'] = i
        results[-1]['min_length'] = min(res)
        results[-1]['max_length'] = max(res)
        results[-1]['average'] = round(sum(res) / len(res))

with open('sounds.json', 'w') as output:
    json.dump(results, output, indent=4)


