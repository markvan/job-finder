from bs4 import BeautifulSoup
from src.application.cwjobspagegetter import CWJobsPageGetter


class JobFormatter:
    @staticmethod
    def select(job):
        # build the job div
        out = ""
        if JobFormatter.is_contract(job):
            out = "<div class='job'>"
            out += JobFormatter.heading(job)
            out += '<div class="notes">'
            out += '<div class="textbox">'
            out += '<p class="alignleft">' + JobFormatter.salary(job) + '</p>'
            out += '<p class="alignright">' + JobFormatter.when(job) + '</p>'
            out += '</div><div style="clear: both;"></div>'
            out += '<p>' + JobFormatter.location(job) + '</p>'
            out += '</div>'
            out += str(JobFormatter.job_description(job))
            out += "</div>"
            out = out.replace('...', "").replace('…',"").replace('  ', ' ').replace(" ", ' ')
            #TODO messy clean up
            out = out.replace('<br/><br/>', '<br/>').replace('<br/> <br/>', '<br/>').replace('<p><p/>', "")
        return out

    @staticmethod
    def heading(job):
        out = str(job.find('div', class_='job-title'))
        out = out.replace('<a ', '<a target="_blank" rel="noopener noreferrer" ')
        out = out.replace('<span class="label label-featured">Featured</span>', "")
        out = out.replace('<span class="label label-featured">Premium</span>', "")
        return out


    @staticmethod
    def job_description(job):
        # fid the url for the job
        url = job.find('div', class_='job-title').find('a')['href']
        # get the job page html
        job_page = CWJobsPageGetter.get(url)
        soup = BeautifulSoup(job_page, 'html.parser')
        # return the job description
        return soup.find('div', class_='job-description')

    @staticmethod
    def is_contract(job):
        job_type = str(job.find('li', class_='job-type').text)
        return 'Contract' in job_type

    @staticmethod
    def salary(job):
        return str(job.find('li', class_='salary').text)

    @staticmethod
    def location(job):
        out = str(job.find('li', class_='location').text)
        return out.replace('from', "").replace('- Update', "").replace('Update', "")

    @staticmethod
    def when(job):
        return str(job.find('li', class_='date-posted').text)

