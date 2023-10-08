from bs4 import BeautifulSoup
import datetime
import contextlib
import pathlib
import sys


from bookmark import Bookmark
from bookmarks_extractor import BookmarksExtractor
from markdown_generator import MarkdownGenerator


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: python chrome-bookmarks-extractor.py <input-file> [output-file]')
        sys.exit(1)
    
    input_filename = pathlib.Path(sys.argv[1])
    if not input_filename.exists():
        print(f'File "{input_filename}" does not exist.')
        sys.exit(1)
    
    extractor = BookmarksExtractor()
    bookmarks = extractor.extract_bookmarks(input_filename)#.sort(key=lambda bookmark: bookmark.date)
    markdown_generator = MarkdownGenerator()
    markdown = markdown_generator.generate_markdown(bookmarks)

    if len(sys.argv) == 3:
        output_filename = pathlib.Path(sys.argv[2])
        with contextlib.ExitStack() as stack:
            file = stack.enter_context(open(output_filename, 'w', encoding='utf-8'))
            file.write(markdown)
    else:
        print(markdown)