from pathlib import Path
from bs4 import BeautifulSoup
from bookmark import Bookmark
import datetime
import contextlib
import typing


class BookmarksExtractor:
    def extract_bookmarks(self, filename: Path) -> typing.List[Bookmark]:
        with contextlib.ExitStack() as stack:
            file = stack.enter_context(open(filename, "r", encoding="utf-8"))
            return self.__parse_file(file)

    def __parse_file(self, file) -> typing.List[Bookmark]:
        soup = BeautifulSoup(file, "html5lib") # html.parser, html5lib         
        bookmarks = []
        for link in soup.find_all("a"):
            href = link.get("href")
            add_date = link.get("add_date")
            date = self.__parse_date(add_date)
            parent_title = link.find_parent().find_parent().find_parent().find_next("h3").text
            bookmark = Bookmark(link.text, href, date, parent_title)
            bookmarks.append(bookmark)
        return bookmarks

    @staticmethod
    def __parse_date(timestamp: str) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(int(timestamp))
