__author__ = 'Blayne'
#Retrieve info on club

from src import Scraper
from BeautifulSoup import BeautifulSoup


class ClubInfo:
    def __init__(self, url):
        global bs
        s = Scraper(url)
        bs = BeautifulSoup(s.get_html())

    @staticmethod
    def __get_fixtures():
        links = bs.findAll("a")
        for link in links:
            if link.text == "Fixtures":
                return "http://www.transfermarkt.co.uk"+link.get('href')

    #return number of games played by club *90 (total minutes)
    def get_mins(self):
        url = self.__get_fixtures()
        s = Scraper(url)
        bs_local = BeautifulSoup(s.get_html())
        tables = bs_local.findAll("table")
        return int(tables[3].findAll('tr')[3].findAll('td')[1].string) * 90
