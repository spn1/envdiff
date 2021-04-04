from loader import Loader

class Diff():
    def __init__(self, left_file, right_file):
        file_loader = Loader()
        self.left = file_loader.read_file_contents(left_file)
        self.left_dict = self.convert_to_dict(self.left, '=')
        # self.right = self.read_file_contents(right_file)

        print(self.left, '\n')
        print(self.left_dict, '\n')
        # print(self.right)

    def convert_to_dict(self, contents, delimiter):
        return dict(line.split(delimiter) for line in contents)

    def diff(self):
        pass
