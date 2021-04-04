class Loader():
    def __init__(self):
        pass

    def read_file_contents(self, filename):
        """
        Reads and Returns the contents of a file
        Returns an array, where each line in the file is a value in the array
        """
        with open(filename, mode='r', encoding='utf-8') as file:
            contents = file.read().splitlines()

        contents = list(filter(lambda item: item, contents))

        return self.trim(contents)

    def trim(self, contents):
        """ 
        Gets rid of unnecesary lines from file contents and returns the result
        E.G. Comments, New Lines
        """
        return list(filter(self.line_filter, contents))

    def line_filter(self, line):
        """
        Determines which lines in the file to filter out (comments)
        """
        return line[0] != '#'