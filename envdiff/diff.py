from envdiff.loader import Loader

class Diff():
    def __init__(self, left_file, right_file):
        file_loader = Loader()

        # Read lines from files into object properties
        self.left = file_loader.read_file_contents(left_file)
        self.right = file_loader.read_file_contents(right_file)

    def convert_to_dict(self, contents, delimiter):
        return dict(line.split(delimiter) for line in contents)

    def diff(self):
        # Convert file contents to Dictionaries
        left_dict = self.convert_to_dict(self.left, '=')
        right_dict = self.convert_to_dict(self.right, '=')

        # Find shared & unique keys in each Dictionary
        shared_keys = self.find_distinct_shared_keys(left_dict, right_dict)
        unique_keys = self.find_unique_keys(left_dict, right_dict)

        # Attach values to shared & unique keys
        # shared = { 'key': { 'left_value', 'right_value' }, ... }
        # unique = { 'left': { 'key': 'value', ... }, 'right': { 'key': 'value', ...} }
        shared_list = { key: { 'left': left_dict[key], 'right': right_dict[key] } for key in shared_keys }
        unique_list = { 'left': { key: left_dict[key] for key in unique_keys['left']}, 'right': { key: right_dict[key] for key in unique_keys['right'] } }

        return shared_list, unique_list

    def find_unique_keys(self, left_dict, right_dict):
        # Convert list of keys to Sets
        left_keys = set(left_dict.keys())
        right_keys = set(right_dict.keys())

        # Find unique keys between Sets
        left_unique = left_keys - right_keys
        right_unique = right_keys - left_keys

        return { 'left': list(left_unique), 'right': list(right_unique) }

    def find_distinct_shared_keys(self, left_dict, right_dict):
        # Convert list of keys to Sets
        left_keys = set(left_dict.keys())
        right_keys = set(right_dict.keys())

        # Find common keys between Sets
        shared_keys = left_keys.intersection(right_keys)

        # Find out which shared keys contain different values between the Dictionaries
        return [ key for key in shared_keys if left_dict[key] != right_dict[key] ]
