import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--per-day', type=float, default=99999)
parser.add_argument('--per-week', type=float, default=99999)
parser.add_argument('--per-month', type=float, default=99999)
parser.add_argument('--per-year', type=float, default=99999)
parser.add_argument('--get-by', choices=['day', 'month', 'year'], default='day')
args = parser.parse_args()
if args.get_by == 'year':
    print(int(args.per_year))
elif args.get_by == 'month':
    print(int(args.per_month))
elif args.get_by == 'day':
    print(int(args.per_day))
