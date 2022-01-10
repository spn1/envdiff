from envdiff.loader import Loader

class Diff():
    def __init__(self, left_file, right_file, comment='#', separator='='):
        """
        Initialise this class object
        :left_file, The name of the first file
        :right_file, The name of the second file
        :comment, The characters used to indicate a comment
        :separator, The characters used to indicate the key-value pair
        """
        self.separator_char = separator

        # Read lines from files into object properties
        file_loader = Loader(comment)
        self.left = file_loader.get_lines_of_interest(left_file)
        self.right = file_loader.get_lines_of_interest(right_file)

    def convert_to_dict(self, lines, delimiter):
        """
        Converts a list of strings and separates them into
        key-value pairs (in a dictionary)
        :lines, The list of strings to convert
        :delimiter, The character(s) to separate the key-value pairs by
        :return, A dictionary of the key-value pairs
        """
        return dict(line.split(delimiter, 1) for line in lines)

    def diff(self):
        """
        Using the files previous loaded in the constructor, will return two
        dicts: one detailing any unique keys found only in one of the files,
        and another detailing any shared keys between the two files, and the
        corresponding values of each.
        :return, (shared_keys) The dictionary of shared keys;
                 (unique_keys) The dictionary of unique keys;
        """
        # Convert file contents to Dictionaries
        left_dict = self.convert_to_dict(self.left, self.separator_char)
        right_dict = self.convert_to_dict(self.right, self.separator_char)

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
        """
        Find the unique keys between two dictionaries
        :left_dict, The first dictionary to compare
        :right_dict, The second dictionary to compare
        :return, A dictionary containing the unique keys in each file, in the format:
                 { 'left': [ ...keys ], 'right': [ ...keys ] }
        """
        # Convert list of keys to Sets
        left_keys = set(left_dict.keys())
        right_keys = set(right_dict.keys())

        # Find unique keys between Sets
        left_unique = left_keys - right_keys
        right_unique = right_keys - left_keys

        return { 'left': list(left_unique), 'right': list(right_unique) }

    def find_distinct_shared_keys(self, left_dict, right_dict):
        """
        Find the shared keys between two dictionaries that have different values
        :left_dict, The first dictionary to compare
        :right_dict, The second dictionary to compare
        :return, A dictionary containing the different shared keys in each file, in the format:
                 { key: { left: 'value-1', right: 'value-2' }, ... }
        """
        # Convert list of keys to Sets
        left_keys = set(left_dict.keys())
        right_keys = set(right_dict.keys())

        # Find common keys between Sets
        shared_keys = left_keys.intersection(right_keys)

        # Find out which shared keys contain different values between the Dictionaries
        return [ key for key in shared_keys if left_dict[key] != right_dict[key] ]
