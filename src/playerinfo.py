__author__ = 'Blayne'
#retrive the player information

from src import Scraper
from BeautifulSoup import BeautifulSoup


class PlayerParser:
    def __init__(self, url):
        global bs
        global global_url
        global tables
        global_url = url
        s = Scraper(url)
        bs = BeautifulSoup(s.get_html())
        tables = self.get_tables()

    @staticmethod
    def get_tables():
        return bs.findAll("table", {"class": "profilheader"})

    @staticmethod
    def get_name():
        s = global_url[31:]
        s = s[0:s.index("/")]
        return s.replace("-", " ")

    @staticmethod
    def get_age():
        return tables[0].findAll('tr')[1].findAll('td')[0].string

    @staticmethod
    def get_club():
        s = tables[1].findAll('tr')[1].findAll('td')[0].find('a')
        return s.get('href')

    @staticmethod
    def get_details():
        info = [None] * 14
        i = 0
        table = bs.find("table", {"class": "items"})
        for row in table.findAll("tr"):
            for cell in row.findAll("td"):
                info[i] = cell.string
                i += 1
        return info


class PlayerInfo:
    def __init__(self, url):
        global playerinfo
        global p
        p = PlayerParser(url)
        playerinfo = p.get_details()

    @staticmethod
    def get_name():
        return p.get_name()

    @staticmethod
    def get_age():
        return p.get_age()

    @staticmethod
    def get_club():
        return p.get_club()

    @staticmethod
    def get_app():
        return playerinfo[0]

    @staticmethod
    def get_goal():
        return playerinfo[1]

    @staticmethod
    def get_assist():
        return playerinfo[2]

    @staticmethod
    def get_yellow():
        return playerinfo[3]

    @staticmethod
    def get_yellred():
        return playerinfo[4]

    @staticmethod
    def get_red():
        return playerinfo[5]

    @staticmethod
    def get_mins():
        s = playerinfo[6].replace("'", "")
        return s.replace(".", "")