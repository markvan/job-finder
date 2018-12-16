import urllib.request
from bs4 import BeautifulSoup


class CWPages:
    def __init__(self, url):
        self.url = url


    def get_page(self):
        with urllib.request.urlopen(self.url) as url:
            self.contents = url.read()

    def get_page_results(self):
        self.get_page()
        soup = BeautifulSoup(self.contents, 'html.parser')
        out = ""
        for link in soup.find('div', class_="job-results").find_all('div', class_="job new "):
            out += str(link.find('a'))
            out += str(link.find('p', class_="job-intro"))
        print(out)


url_result = CWPages("https://www.cwjobs.co.uk/jobs/contract/innovation/in-london?postedwithin=1")
url_result.get_page_results()