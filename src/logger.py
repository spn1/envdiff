from rich import print
from rich.console import Console
from rich.table import Table
from rich.table import Column
from rich.style import Style
from rich import box

class Logger():
    def __init__(self):
        """ Initialize console & styles """
        self.console = Console(style='frame')
        self.left_style = Style(color='red')
        self.right_style = Style(color='yellow')

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
        self.console.print(f'Files to Compare\n[red]{args[0]}[/red] & [yellow]{args[1]}[/yellow]', justify='center')

    def print_diff(self, shared, unique, left_filename, right_filename):
        """ 
        Log the main output of the program
        :shared, The dictionary of shared env vars
        :unique, The dictionary of unique env vars
        """
        # shared = { 'key': { 'left_value', 'right_value' }, ... }
        # unique = { 'left': { 'key': 'value', ... }, 'right': { 'key': 'value', ...} }
        self.console.rule()
        self.print_shared_table(shared, left_filename, right_filename)
        self.console.rule()
        self.print_unique_table(unique, left_filename, right_filename)
        self.console.rule()

    def print_shared_table(self, shared, left_filename, right_filename):
        """
        Log the table displaying the shared environment variable differences
        :shared, The dictionary of shared environment variables
        :left_filename, The filename of the first file
        :right_filename, The filename of the second file
        """
        table = Table(title='Shared Environment Variables', box=box.ROUNDED, header_style='bold', expand=True)

        table.add_column('Variable', justify='right', style='cyan', header_style='white')
        table.add_column(f'{left_filename}', style=self.left_style, header_style='white')
        table.add_column(f'{right_filename}', style=self.right_style, header_style='white')

        for key in dict(sorted(shared.items())):
            table.add_row(key, shared[key]['left'], shared[key]['right'])

        self.console.print(table)

    def print_unique_table(self, unique, left_filename, right_filename):
        """
        Log the table displaying the shared environment variable differences
        :unique, The dictionary of unique environment variables
        :left_filename, The filename of the first file
        :right_filename, The filename of the second file
        """
        table = Table(title='Unique Environment Variables', box=box.ROUNDED, header_style='bold', expand=True)

        table.add_column(f'{left_filename}', justify='right', style='cyan', header_style='white')
        table.add_column('Value', style=self.left_style, header_style='white')
        table.add_column(f'{right_filename}', justify='left', style='magenta', header_style='white')

        for k, v in sorted(unique['left'].items()):
            table.add_row(k, v, '')

        for k, v in sorted(unique['right'].items()):
            table.add_row('', v, k)

        self.console.print(table)
