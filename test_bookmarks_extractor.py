import unittest

from chrome_bookmarks_extractor import BookmarksExtractor

class TestBookmarksExtractor(unittest.TestCase):
    def test_extract_bookmarks(self):
        extractor = BookmarksExtractor()
        bookmarks = extractor.extract_bookmarks('bookmarks.html')
        self.assertEqual(len(bookmarks), 377)

if __name__ == '__main__':
    unittest.main()