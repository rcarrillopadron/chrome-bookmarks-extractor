from bs4 import BeautifulSoup
from datetime import datetime
import contextlib
import datetime
import pathlib
import sys
import typing

class Bookmark(typing.NamedTuple):
    text: str
    href: str
    date: datetime.datetime

    def get_domain(self) -> str:
        return self.href.split('/')[2]

    def get_readable_date(self) -> str:
        return self.date.strftime('%Y-%m-%d')


class BookmarksExtractor:
    def extract_bookmarks(self, filename: str) -> typing.List[Bookmark]:
        with contextlib.ExitStack() as stack:
            file = stack.enter_context(open(filename, 'r', encoding='utf-8'))
            return self.__parse_file(file)

    def __parse_file(self, file) -> typing.List[Bookmark]:
        soup = BeautifulSoup(file, 'html.parser')
        bookmarks = []
        for link in soup.find_all('a'):
            href = link.get('href')
            add_date = link.get("add_date")
            date = self.__parse_date(add_date)
            bookmark = Bookmark(link.text, href, date)
            bookmarks.append(bookmark)
        return bookmarks

    def __parse_date(self, timestamp: str) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(int(timestamp))

class MarkdownGenerator:
    def generate_markdown(self, bookmarks: typing.List[Bookmark]) -> str:
        markdown_table = self.generate_markdown_table(bookmarks)
        return f"# Bookmarks\n\n{markdown_table}\n\nGenerated by [{__file__}]"

    def generate_markdown_table(self, bookmarks: typing.List[Bookmark]) -> str:
        lines = []
        lines.append("| # | Domain | Date | Bookmark |")
        for index, bookmark in enumerate(bookmarks):
            line = self.generate_row(index, bookmark)
            lines.append(line)
        return '\n'.join(lines)

    def generate_row(self, index: int, bookmark: Bookmark) -> str:
        domain = bookmark.get_domain()
        readable_date = bookmark.get_readable_date()
        return f"| {index} | {domain} | {readable_date} | [{bookmark.text}]({bookmark.href}) |"

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