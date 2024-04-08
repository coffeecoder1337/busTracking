from bs4 import BeautifulSoup as BS
import requests


class Parser:
    def __init__(self, url):
        self.url = url
        self.soup = self.get_soup()

    def get_soup(self):
        return BS(requests.get(self.url).text, 'lxml')

    def parse_time(self):
        rows = [row.text.strip() for row in self.soup.find_all('tr')[1:]]
        return rows
