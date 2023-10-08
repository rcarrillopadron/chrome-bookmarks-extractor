from bs4 import BeautifulSoup
import datetime
import contextlib
import typing

from bookmark import Bookmark


class BookmarksExtractor:
    def extract_bookmarks(self, filename: str) -> typing.List[Bookmark]:
        with contextlib.ExitStack() as stack:
            file = stack.enter_context(open(filename, "r", encoding="utf-8"))
            return self.__parse_file(file)

    def __parse_file(self, file) -> typing.List[Bookmark]:
        soup = BeautifulSoup(file, "html.parser")
        bookmarks = []
        for link in soup.find_all("a"):
            href = link.get("href")
            add_date = link.get("add_date")
            date = self.__parse_date(add_date)
            bookmark = Bookmark(link.text, href, date)
            bookmarks.append(bookmark)
        return bookmarks

    def __parse_date(self, timestamp: str) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(int(timestamp))
