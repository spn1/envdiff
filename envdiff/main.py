from sys import argv
from diff import Diff
from logger import Logger

if __name__ == '__main__':
    try:
        args = argv[1:3]
        
        logger = Logger()
        logger.print_title()
        logger.print_args(args)        

        differ = Diff(left_file=args[0], right_file=args[1])
        shared, unique = differ.diff()

        logger.print_diff(shared, unique, left_filename=args[0], right_filename=args[1])
    except IndexError:
        raise SystemExit(f'Usage: {argv[0]} <file> <file>')
    except FileNotFoundError:
        raise SystemExit(f'File not found')