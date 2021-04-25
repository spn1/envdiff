import unittest

from envdiff.loader import Loader

class TestLoader(unittest.TestCase):
    def setUp(self):
        self.loader = Loader()
        self.loader.read_file_contents('test/fixtures/.env-dev')
    
    def test_opens_file(self):
        # Mock python open function?
        pass

    def test_does_not_include_commented_lines(self):
        pass

    def test_does_not_include_comments_that_follow_values(self):
        pass

    def test_line_filter(self):
        test_line = 'ENDPOINT=https://www.google.com/'
        test_comment = '# This is a comment'

        self.assertEqual(self.loader.line_filter(test_line), True)
        self.assertEqual(self.loader.line_filter(test_comment), False)

    def tearDown(self):
        self.loader = None

if __name__ == '__main__':
    unittest.main()