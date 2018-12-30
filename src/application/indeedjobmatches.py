from src.application.indeedjobformatter import IndeedJobFormatter
import urllib.request
from bs4 import BeautifulSoup


class IndeedJobMatches:

    # allow iteration over jobs for a search url
    def next_job(self, url):
        for job in self._get_all_jobs(url).find_all('div', class_="result"):
            formatted_job = IndeedJobFormatter.format(job)
            yield formatted_job

    # extract all jobs from one or more search result pages
    def _get_all_jobs(self, url):
        number_of_jobs_on_page = -1
        out = ""
        u = url
        while number_of_jobs_on_page != 0:
            jobs = str(self._get_jobs_from_page(u))
            number_of_jobs_on_page = 0  # jobs.count('class="job new " id=')
            out += jobs
            # u = self._make_next_url(u)
        return BeautifulSoup(out, 'html.parser')

    # returns 0 to many jobs from a page at the url
    def _get_jobs_from_page(self, url):
        soup = BeautifulSoup(self._get_html(url), 'html.parser')
        out = ""
        interim = soup.find('td', {"id": "resultsCol" })
        for link in interim.find_all('div', class_="result"):
            out += str(link)
        return BeautifulSoup(out, 'html.parser')
        # get page source at the url

    def _get_html(self, url):
        with urllib.request.urlopen(url) as u:
            page_source = u.read()
        return page_source

    def _make_next_url(self, url):
        if "&page=" in url:
            page = int(url[-1:])
            u = url[:-1]+str(page+1)
        else:
            u = url+"&page=2"
        return u

#TODO new sponsored jobs may not have class "job new" check on these

#TODO start working with search string, not url, at least in next_job and _get_all_jobs

#TODO the current implementation of next job gets all pages of jobs at once via _get_all_jobs
#    it would be better to get pages of jobs as needed by next_job during its repeated invocations
