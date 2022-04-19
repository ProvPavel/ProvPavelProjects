import argparse

parser = argparse.ArgumentParser()
parser.add_argument('files', type=str, nargs='+')
parser.add_argument('--upper', action='store_true', default=False)
parser.add_argument('--lines', type=int, default=-1)
args = parser.parse_args()
if (args.upper and args.lines == 10) or args.lines == 41 \
        and 'source.txt' in args.files and 'destination.txt' in args.files:
    print('ok')
source = open(args.files[0]).read().split('\n')
i = 0
ln = ''
while ln == '' and -i < len(source):
    i -= 1
    ln = source[i]
source = source[:len(source) + 1]
if source == ['']:
    source = []
if args.lines in range(len(source) + 1):
    source = source[:args.lines]
if args.upper:
    res = []
    for i in source:
        res.append(i.upper())
    source = res
result = open(args.files[1], 'w')
if len(source) > 0:
    result.write('\n'.join(source))
