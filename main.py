import argparse
from sys import argv
from envdiff.diff import Diff
from envdiff.logger import Logger

def main():
    parser = argparse.ArgumentParser(description="""
        Processes two environment files to determine
        differences between the same keys
        """
    )
    parser.add_argument(
        '-c',
        '--comment',
        help='Define the characters used to begin a comment',
        default='#'
    )
    parser.add_argument(
        '-s',
        '--separator',
        help='Define the characters used to separate the key-value pairs',
        default='='
    )
    parser.add_argument('left', help='The filename of the first file')
    parser.add_argument('right', help='The filename of the second file')

    try:
        # Get command-line arguments
        args = vars(parser.parse_args())
        left_file = args['left'];
        right_file = args['right'];
        comment = args['comment']
        separator = args['separator']

        # Initialise results logger
        logger = Logger()
        logger.print_title()

        # Do the diffing
        differ = Diff(
            left_file=left_file,
            right_file=right_file,
            comment=comment,
            separator=separator
        )

        shared, unique = differ.diff()

        # Print results
        logger.print_diff(shared, unique, left_filename=left_file, right_filename=right_file)
    except IndexError:
        raise SystemExit(f'Usage: {argv[0]} <file> <file>')
    except FileNotFoundError:
        raise SystemExit(f'File not found')

if __name__ == '__main__':
    main()