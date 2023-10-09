import datetime
import typing


class Bookmark(typing.NamedTuple):
    text: str
    href: str
    date: datetime.datetime
    parent_title: str

    def get_domain(self) -> str:
        return self.href.split("/")[2]

    def get_readable_date(self) -> str:
        return self.date.strftime("%Y-%m-%d")
