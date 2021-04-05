from sys import argv
from diff import Diff
from logger import Logger

try:
    logger = Logger()
    logger.print_title()

    args = argv[1:3]
    logger.print_args(args)

    differ = Diff(left_file=args[0], right_file=args[1])
    shared, unique = differ.diff()

    # logger.print(shared)
    # logger.print(unique)

    logger.print_diff(shared, unique, left_filename=args[0], right_filename=args[1])

except IndexError:
    raise SystemExit(f'Usage: {argv[0]} <file> <file>')
except FileNotFoundError:
    raise SystemExit(f'File not found')
