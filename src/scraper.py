__author__ = 'Blayne'

import urllib2


class Scraper:
    def __init__(self, url):
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        response = opener.open(url)
        self.f = response.read()

    def get_html(self):
        return self.f
