class Loader():
    def __init__(self, comment='#'):
        self.comment_char = comment

    def read_file_contents(self, filename):
        """
        Reads and Returns the contents of a file
        :filename, The name of the file to be read
        :return, An array container each line in the file, trimmed to remove comments and newlines
        """
        # Read lines from file
        with open(filename, mode='r', encoding='utf-8') as file:
            contents = file.read().splitlines()

        return contents

    def comment_filter(self, line):
        """
        Determines which lines in the file to filter out (comments)
        :line, The line to be filtered
        :return, True or False if the line should be kept in the result
        """
        comment_char_len = len(self.comment_char)

        return line[:comment_char_len] != self.comment_char

    def get_lines_of_interest(self, filename):
        """
        Reads the given filename and returns only the lines
        of interest - I.E. the ones with key-value pairs in them
        :filename, The name of the file to be opened
        """
        file_contents = self.read_file_contents(filename)

         # Removes empty lines
        contents = list(filter(lambda item: item, file_contents))

        # Remove commented out lines
        contents = list(filter(self.comment_filter, contents))

        # Trim lines with comments at the end
        contents = [ line.split(f' {self.comment_char}')[0] for line in contents ]

        return contents