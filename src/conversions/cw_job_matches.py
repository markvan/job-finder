import urllib.request
from bs4 import BeautifulSoup


class CWJobMatches:
    # get page source at the url
    def get_html(self, url):
        with urllib.request.urlopen(url) as u:
            page_source = u.read()
        return page_source

    # returns 0 to many jobs from a page at the url
    def get_jobs(self, url):

        soup = BeautifulSoup(self.get_html(url), 'html.parser')
        out = ""
        for link in soup.find('div', class_="job-results").find_all('div', class_="job new "):
            out += str(link.find('a'))
            out += str(link.find('p', class_="job-intro"))
        return out
