from sys import argv
from diff import Diff

try:
    args = argv[1:3]

    differ = Diff(left_file=args[0], right_file=args[1])

    shared, unique = differ.diff()

    print('Shared: ', shared, '\n')
    print('Unique: ', unique, '\n')

    print()
except IndexError:
    raise SystemExit(f'Usage: {argv[0]} <file> <file>')
