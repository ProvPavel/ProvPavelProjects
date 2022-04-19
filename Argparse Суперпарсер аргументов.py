import sys
import argparse

ln = len(sys.argv) - 1
parser = argparse.ArgumentParser()
if sys.argv[-1] in ('-h', '--help'):
    print("""usage: solution.py [-h] [arg ...]

positional arguments:
  arg

optional arguments:
  -h, --help  show this help message and exit""")
elif ln > 0:
    parser.add_argument('arg', type=str, nargs='+')
    args = parser.parse_args()
    print('\n'.join(args.arg))
else:
    print('no args')
