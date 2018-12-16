import urllib.request
from bs4 import BeautifulSoup


class CWJobMatches:
    def __init__(self, url):
        self.url = url

    def get_html(self):
        with urllib.request.urlopen(self.url) as url:
            page_source = url.read()
        return page_source

    def get_jobs(self):
        soup = BeautifulSoup(self.get_html(), 'html.parser')
        out = ""
        for link in soup.find('div', class_="job-results").find_all('div', class_="job new "):
            out += str(link.find('a'))
            out += str(link.find('p', class_="job-intro"))
        return out


job_matcher = CWJobMatches("https://www.cwjobs.co.uk/jobs/contract/innovation/in-london?postedwithin=1")
print(job_matcher.get_jobs())
