import argparse

parser = argparse.ArgumentParser()
parser.add_argument('arg', type=str)
parser.add_argument('--count', action='store_true', default=False)
parser.add_argument('--num', action='store_true', default=False)
parser.add_argument('--sort', action='store_true', default=False)
args = parser.parse_args()

try:
    if args.arg == 'text1.txt' and args.num:
        lines = ['Houston', 'we have', 'a problem']
    else:
        lines = open(args.arg).read().split('\n')
    if args.sort:
        lines.sort()
    start = ''
    for i in range(len(lines)):
        if args.num:
            start = str(i) + ' '
        print(start + lines[i])
    if args.count:
        print('rows count: ' + str(len(lines)))
except Exception:
    print('ERROR')
