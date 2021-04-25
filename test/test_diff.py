import unittest

from envdiff.diff import Diff

class TestDiff(unittest.TestCase):
    def test_loads_files_on_construction(self):
        expected_contents = ['URL=https://www.test.com/']

        self.differ = Diff('test/fixtures/.env-simple', 'test/fixtures/.env-simple')

        self.assertEqual(self.differ.left, expected_contents)
        self.assertEqual(self.differ.right, expected_contents)

    def test_files_are_indentical(self):
        self.differ = Diff('test/fixtures/.env-simple', 'test/fixtures/.env-simple')


    def test_highlights_differences_between_shared_keys(self):
        pass

    def test_highlights_unique_keys(self):
        pass

    def tearDown(self):
        self.differ = None

if __name__ == '__main__':
    unittest.main()