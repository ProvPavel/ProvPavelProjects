import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--barbie', metavar='b', type=int, default=50)
parser.add_argument('--cars', metavar='c', type=int, default=50)
parser.add_argument('--movie', metavar='m', type=str, default='other')
args = parser.parse_args()
if args.barbie not in range(101):
    args.barbie = 50
if args.cars not in range(101):
    args.cars = 50
if args.movie == 'melodrama':
    m = 0
if args.movie == 'football':
    m = 100
else:
    m = 50
boy = round((100 - args.barbie + args.cars + m) / 3)
girl = 100 - boy
print('boy:', boy)
print('girl:', girl)
