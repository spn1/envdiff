import unittest

from envdiff.loader import Loader

class TestLoader(unittest.TestCase):
    def setUp(self):
        self.loader = Loader()

    def test_opens_file(self):
        # Mock python open function?
        expected = ['URL=https://www.test.com/', 'FOO=BAR']

        result = self.loader.read_file_contents('test/fixtures/.env-simple')

        self.assertEqual(result, expected)

    def test_does_not_include_commented_lines_or_new_lines(self):
        expected = ['KEY=VALUE']

        result = self.loader.read_file_contents('test/fixtures/.env-with-comments')

        self.assertEqual(result, expected)
        self.assertFalse(result.count(''))

    @unittest.expectedFailure
    def test_does_not_include_comments_that_follow_values(self):
        expected = ['FOO=BAR']

        result = self.loader.read_file_contents('test/fixtures/.env-with-inline-comment')

        self.assertEqual(result, expected)

    def test_comment_filter(self):
        test_line = 'ENDPOINT=https://www.google.com/'
        test_comment = '# This is a comment'

        self.assertEqual(self.loader.comment_filter(test_line), True)
        self.assertEqual(self.loader.comment_filter(test_comment), False)

    def tearDown(self):
        self.loader = None

if __name__ == '__main__':
    unittest.main()