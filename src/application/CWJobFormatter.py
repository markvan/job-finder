from bs4 import BeautifulSoup
from src.application.cwjobspagegetter import CWJobsPageGetter


class CWJobFormatter:
    @staticmethod
    def format(job):
        # build the job div
        out = ""
        if CWJobFormatter._is_contract(job):
            out = "<div class='job'>"
            out += CWJobFormatter._heading(job)
            out += '<div class="notes">'
            out += '<div class="textbox">'
            out += '<p class="alignleft">' + CWJobFormatter._salary(job) + '</p>'
            out += '<p class="alignright">' + CWJobFormatter._date_posted(job) + '</p>'
            out += '</div><div style="clear: both;"></div>'
            out += '<p>' + CWJobFormatter._location(job) + '</p>'
            out += '</div>'
            out += str(CWJobFormatter._description(job))
            out += "</div>"
            out = out.replace('...', "").replace('…',"").replace('  ', ' ').replace(" ", ' ')
            #TODO messy clean up
            out = out.replace('<br/><br/>', '<br/>').replace('<br/> <br/>', '<br/>').replace('<p><p/>', "")
        return out

    @staticmethod
    def _heading(job):
        out = str(job.find('div', class_='job-title'))
        out = out.replace('<a ', '<a target="_blank" rel="noopener noreferrer" ')
        out = out.replace('<span class="label label-featured">Featured</span>', "")
        out = out.replace('<span class="label label-featured">Premium</span>', "")
        return out



    # this finds the job description from the page at the url in the search results
    @staticmethod
    def _description(job):
        # fid the url for the job
        url = job.find('div', class_='job-title').find('a')['href']
        # get the job page html
        job_page = CWJobsPageGetter.get(url)
        soup = BeautifulSoup(job_page, 'html.parser')
        # return the job description
        return soup.find('div', class_='job-description')

    # remaining methods just get info from the job description in the search results
    @staticmethod
    def _is_contract(job):
        job_type = str(job.find('li', class_='job-type').text)
        return 'Contract' in job_type

    @staticmethod
    def _salary(job):
        return str(job.find('li', class_='salary').text)

    @staticmethod
    def _location(job):
        out = str(job.find('li', class_='location').text)
        return out.replace('from', "").replace('- Update', "").replace('Update', "")

    @staticmethod
    def _date_posted(job):
        return str(job.find('li', class_='date-posted').text)

