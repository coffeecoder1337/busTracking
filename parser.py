from bs4 import BeautifulSoup as BS
import requests


class Parser:
    def __init__(self, url: str):
        self.url = url
        self._soup = self._get_soup()

    def _get_soup(self):
        return BS(requests.get(self.url).text, 'lxml')

    def parse_time(self) -> list[str]:
        rows = [row.text.strip() for row in self._soup.find_all('tr')[1:]]
        return rows
