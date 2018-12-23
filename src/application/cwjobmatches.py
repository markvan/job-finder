import urllib.request
from bs4 import BeautifulSoup
from src.application.jobFormatter import JobFormatter
from src.application.cwjobspagegetter import CWJobsPageGetter

import urllib.request
import os


#TODO new sponsored jobs may not have class "job new" check on these

#TODO start working with search string, not url, at least in next_job and get_all_jobs

#TODO the current implementation of next job gets all pages of jobs at once via get_all_jobs
#    it would be better to get pages of jobs as needed by next_job during its repeated invocations

class CWJobMatches:
    # get page source at the url
    def get_html(self, url):
        with urllib.request.urlopen(url) as u:
            page_source = u.read()
        return page_source

    def get_html2(self, url):
        return CWJobsPageGetter.get('https://www.cwjobs.co.uk/job/digital-business-analyst/lorien-resourcing-job84625719')

    # returns 0 to many jobs from a page at the url
    def get_jobs_from_page(self, url):
        soup = BeautifulSoup(self.get_html(url), 'html.parser')
        out = ""
        for link in soup.find('div', class_="job-results").find_all('div', class_="job new "):
            out += str(link)
        return BeautifulSoup(out, 'html.parser')

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
        while last_count != 0:
            jobs = str(self.get_jobs_from_page(u))
            out += jobs
            last_count = jobs.count('class="job new " id=')
            u = self._get_next_url(u)
        return BeautifulSoup(out, 'html.parser')

    def next_job(self, url):
        for job in self.get_all_jobs(url).find_all('div', class_="job new "):
            job = JobFormatter.select(job)
            yield job
