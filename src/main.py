from sys import argv
from diff import Diff

try:
    args = argv[1:3]
    print(f'Args: {args}')
    differ = Diff(left_file=args[0], right_file=args[1])
    print(differ.diff())
except IndexError:
    raise SystemExit(f'Usage: {argv[0]} <file> <file>')
