class Loader():
    def __init__(self):
        pass

    def read_file_contents(self, filename):
        """
        Reads and Returns the contents of a file
        :filename, The name of the file to be read
        :return, An array container each line in the file, trimmed to remove comments and newlines
        """
        with open(filename, mode='r', encoding='utf-8') as file:
            contents = file.read().splitlines()

        contents = list(filter(lambda item: item, contents))

        return self.trim(contents)

    def trim(self, contents):
        """ 
        Gets rid of unnecesary lines from file contents and returns the result
        :contents, The contents of the file
        :return, the filtered file contents
        """
        return list(filter(self.line_filter, contents))

    def line_filter(self, line):
        """
        Determines which lines in the file to filter out (comments)
        :line, The line to be filtered
        :return, True or False if the line should be kept in the result
        """
        return line[0] != '#'