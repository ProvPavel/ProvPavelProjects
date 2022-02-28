import sys

try:
    args = sys.argv[1::]
    for j in args:
        if '.' in j:
            name = j
    file = open(name, 'r').read().split('\n')
    if '--sort' in args:
        file.sort()
    for i in range(len(file)):
        if '--num' in args:
            print(str(i), file[i])
        else:
            print(file[i])
    if '--count' in args:
        print(f'rows count: {len(file)}')
except Exception:
    print('ERROR')
