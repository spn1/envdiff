import unittest

from envdiff.diff import Diff

class TestDiff(unittest.TestCase):
    def test_loads_files_on_construction(self):
        expected_contents = ['URL=https://www.test.com/', 'FOO=BAR']

        self.differ = Diff('test/fixtures/.env-simple', 'test/fixtures/.env-simple')

        self.assertEqual(self.differ.left, expected_contents)
        self.assertEqual(self.differ.right, expected_contents)

    def test_convert_to_dict(self):
        contents = ['FOO=BAR']

        self.differ = Diff('test/fixtures/.env-simple', 'test/fixtures/.env-simple')
        result = self.differ.convert_to_dict(contents, '=')

        self.assertEqual(result, { 'FOO': 'BAR' })

    def test_convert_to_dict_with_alternate_separator(self):
        contents = ['FOO: BAR']

        self.differ = Diff('test/fixtures/.env-simple', 'test/fixtures/.env-simple')
        result = self.differ.convert_to_dict(contents, ': ')

        self.assertEqual(result, { 'FOO': 'BAR' })

    def test_find_unique_keys(self):
        left = { 'FOO': 'BAR', 'LEFT': 'parsnip' }
        right = { 'FOO': 'BAR', 'RIGHT': 'persimmon' }
        expected = { 'left': ['LEFT'], 'right': ['RIGHT'] }

        self.differ = Diff('test/fixtures/.env-simple', 'test/fixtures/.env-simple')
        result = self.differ.find_unique_keys(left, right)

        self.assertEqual(result, expected)

    def test_find_distinct_shared_keys(self):
        left = { 'FOO': 'BAR', 'LEFT': 'parsnip' }
        right = { 'FOO': 'BOO', 'RIGHT': 'persimmon' }
        expected = [ 'FOO' ]

        self.differ = Diff('test/fixtures/.env-simple', 'test/fixtures/.env-simple')
        result = self.differ.find_distinct_shared_keys(left, right)

        self.assertEqual(result, expected)

    def test_files_are_indentical(self):
        left = { 'FOO': 'BAR' }
        right = { 'FOO': 'BAR' }

        self.differ = Diff('test/fixtures/.env-simple', 'test/fixtures/.env-simple')

        self.assertEqual(self.differ.find_unique_keys(left, right), { 'left': [], 'right': [] })
        self.assertEqual(self.differ.find_distinct_shared_keys(left, right), [])

    def test_diff_with_indentical_files(self):
        self.differ = Diff('test/fixtures/.env-simple', 'test/fixtures/.env-simple')
        shared_list, unique_list = self.differ.diff()

        self.assertEqual(shared_list, {})
        self.assertEqual(unique_list, { 'left': {}, 'right': {} })

    def test_diff_with_files_with_shared_keys_that_differ(self):
        self.differ = Diff('test/fixtures/.env-simple', 'test/fixtures/.env-simple-shared')
        shared_list, unique_list = self.differ.diff()

        self.assertEqual(shared_list, { 'FOO': { 'left': 'BAR', 'right': 'FOO' } })

    def test_diff_with_files_with_unique_keys(self):
        self.differ = Diff('test/fixtures/.env-simple', 'test/fixtures/.env-simple-unique')
        shared_list, unique_list = self.differ.diff()

        self.assertEqual(unique_list, { 'left': { 'FOO': 'BAR' }, 'right': { 'BAR': 'FOO' } })

    def test_diff_with_files_with_unique_and_shared_keys(self):
        self.differ = Diff('test/fixtures/.env-simple', 'test/fixtures/.env-simple-shared-and-unique')
        shared_list, unique_list = self.differ.diff()

        self.assertEqual(shared_list, { 'FOO': { 'left': 'BAR', 'right': 'FOO' } })
        self.assertEqual(unique_list, { 'left': { 'URL': 'https://www.test.com/' }, 'right': { 'BAR': 'FOO' } })

    def test_diff_loading_files_in_opposite_order(self):
        self.differ = Diff('test/fixtures/.env-simple-shared-and-unique', 'test/fixtures/.env-simple')
        shared_list, unique_list = self.differ.diff()

        self.assertEqual(shared_list, { 'FOO': { 'right': 'BAR', 'left': 'FOO' } })
        self.assertEqual(unique_list, { 'right': { 'URL': 'https://www.test.com/' }, 'left': { 'BAR': 'FOO' } })

    def tearDown(self):
        self.differ = None

if __name__ == '__main__':
    unittest.main()