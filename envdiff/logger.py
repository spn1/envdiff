from rich import print
from rich.console import Console
from rich.columns import Columns
from rich.table import Table
from rich.style import Style
from rich import box

class Logger():
    def __init__(self):
        """ Initialize console & styles """
        self.console = Console(style='frame')
        self.left_style = Style(color='orange1')
        self.right_style = Style(color='orange_red1')
        self.variable_style = Style(color='magenta')
        self.header_style = Style(color='white', bold=True)

    def print(self, content):
        """
        Print :content using `rich`
        :content, The content to print
        """
        print(content)

    def print_title(self):
        """ Prints the program title """
        self.console.rule('envdiff')

    def print_args(self, args):
        """
        Print the command-line arguments passed into the tool
        :args, The command-line arguments (array)
        """
        self.console.print(f'Files to Compare\n[orange1]{args[0]}[/orange1] & [orange_red1]{args[1]}[/orange_red1]', justify='center')

    def print_diff(self, shared, unique, left_filename, right_filename):
        """ 
        Log the main output of the program
        :shared, The dictionary of shared env vars
        :unique, The dictionary of unique env vars
        """
        # shared = { 'key': { 'left_value', 'right_value' }, ... }
        # unique = { 'left': { 'key': 'value', ... }, 'right': { 'key': 'value', ...} }
        shared = self.get_shared_table(shared, left_filename, right_filename)
        unique_left, unique_right = self.get_unique_tables(unique, left_filename, right_filename)

        columns = Columns([unique_left, unique_right], expand=True)

        # Do the printing
        self.console.print()
        self.console.print(shared)
        self.console.print()
        self.console.print(columns)

    def get_shared_table(self, shared, left_filename, right_filename):
        """
        Log the table displaying the shared environment variable differences
        :shared, The dictionary of shared environment variables
        :left_filename, The filename of the first file
        :right_filename, The filename of the second file
        """
        table = Table(title='Shared Environment Variables', box=box.ROUNDED, header_style=self.header_style, expand=True)

        table.add_column('Variable', justify='right', style=self.variable_style)
        table.add_column(f'{left_filename}', style=self.left_style)
        table.add_column(f'{right_filename}', style=self.right_style)

        for key in dict(sorted(shared.items())):
            table.add_row(key, shared[key]['left'], shared[key]['right'])

        return table

    def get_unique_tables(self, unique, left_filename, right_filename):
        """
        Log the table displaying the shared environment variable differences
        :unique, The dictionary of unique environment variables
        :left_filename, The filename of the first file
        :right_filename, The filename of the second file
        """
        unique_left = sorted(unique['left'].items())
        unique_right = sorted(unique['right'].items())

        # Create table for left file
        left_table = Table(title=f'Unique {left_filename} Environment Variables', box=box.ROUNDED, header_style=self.header_style, expand=True)
        left_table.add_column('Variable', justify='right')
        left_table.add_column('Value', style='red')

        for k, v in unique_left:
            left_table.add_row(k, v, style=self.left_style)

        # Create table for right file
        right_table = Table(title=f'Unique {right_filename} Environment Variables', box=box.ROUNDED, header_style=self.header_style, expand=True)
        right_table.add_column('Variable', justify='right')
        right_table.add_column('Value', style='red')

        for k, v in unique_right:
            right_table.add_row(k, v, style=self.right_style)

        return left_table, right_table
