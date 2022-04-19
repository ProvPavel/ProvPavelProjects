import sys
import argparse

ln = len(sys.argv) - 1
parser = argparse.ArgumentParser()
if ln > 0:
    parser.add_argument("arg", type=str, nargs='+')
    args = parser.parse_args()
    if len(args.arg) > 2:
        print('TOO MANY PARAMS')
    elif len(args.arg) == 1:
        print('TOO FEW PARAMS')
    else:
        try:
            print(int(args.arg[0]) + int(args.arg[1]))
        except Exception as ex:
            print(str(ex.__class__).split("'")[1])
else:
    print('NO PARAMS')
