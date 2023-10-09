import unittest
import logging
from pathlib import Path
from markdown_generator import MarkdownGenerator
from chrome_bookmarks_extractor import BookmarksExtractor

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

class TestBookmarksExtractor(unittest.TestCase):
    def test_extract_bookmarks(self):
        extractor = BookmarksExtractor()
        items = extractor.extract_bookmarks(Path("bookmarks.html"))
        self.assertEqual(len(items), 376)
        log.debug("HERE")
        for line in MarkdownGenerator.generate_table_header():
            log.debug(line)
        for index, item in enumerate(items):
            row = MarkdownGenerator.generate_row(index + 1, item)
            log.debug(row)

if __name__ == '__main__':
    unittest.main()
