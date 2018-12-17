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
        i = 0
        for link in soup.find('div', class_="job-results").find_all('div', class_="job new "):
            i += 1
            # out += "-----------------" + str(i) + "------"
            out += str(link)
            # out += "-----------------" + str(i) + "------"
        return out

    def _get_next_url(self, url):
        if "&page=" in url:
            page = int(url[-1:])
            u = url[:-1]+str(page+1)
        else:
            u = url+"&page=2"
        return u

    def get_all_jobs(self, url):
        last_count = -1
        out = ""
        u = url
        while (last_count != 0):
            print(u)
            jobs = self.get_jobs(u)
            out += jobs+'''
'''
            last_count = jobs.count('class="job new " id=')
            print(str(last_count)+'\n')
            u = self._get_next_url(u)
        return out
