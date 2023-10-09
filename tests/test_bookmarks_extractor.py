import unittest
from pathlib import Path

from chrome_bookmarks_extractor import BookmarksExtractor


class TestBookmarksExtractor(unittest.TestCase):
    def test_extract_bookmarks(self):
        extractor = BookmarksExtractor()
        bookmarks = extractor.extract_bookmarks(Path("bookmarks.html"))
        self.assertEqual(len(bookmarks), 376)


if __name__ == '__main__':
    unittest.main()
