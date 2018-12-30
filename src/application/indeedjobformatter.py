import urllib.request
from bs4 import BeautifulSoup


class IndeedJobFormatter:

    # job that is being passed around is a beautiful soup object

    @staticmethod
    def format(job):
        out = ""
        if 'a year' not in IndeedJobFormatter._salary(job):
            out = "<div class='job'>"
            out += IndeedJobFormatter._heading(job)
            out += '<div class="notes">'
            out += '<div class="textbox">'
            out += '<p class="alignleft">' + IndeedJobFormatter._salary(job) + '</p>'
            out += '<p class="alignright">' + IndeedJobFormatter._date_posted(job) + '</p>'
            out += '</div><div style="clear: both;"></div>'
            out += '<p>' + IndeedJobFormatter._location(job) + '</p>'
            out += '</div>'
            out += IndeedJobFormatter._description(job)
            out += "</div>"
            out = out.replace('...', "").replace('…', "").replace('  ', ' ').replace(" ", ' ')
            # TODO messy clean up
            out = out.replace('<br/><br/>', '<br/>').replace('<br/> <br/>', '<br/>').replace('<p><p/>', "")
        return out

    @staticmethod
    def _job_page_url(job):
        a_tag = job.find('a')
        href = str(a_tag['href'])
        if '/rc/clk?' in href:
            return href.replace('/rc/clk?', 'https://www.indeed.co.uk/viewjob?')
        if 'https' in href:
            return href
        if '/company/' in href:
            return 'https://www.indeed.co.uk/' + href
        return ""

    @staticmethod
    def _heading(job):
        url = IndeedJobFormatter._job_page_url(job)
        title = str(job.find('a').contents[0])
        out = '<h2><a href="' + url + '" target="_blank" rel="noopener noreferrer" >' + title + '</a></h2>'
        return out

    @staticmethod
    def _description(job):
        out = '<div class ="job-description-cwjobs">'
        # out += job.find('span', class_='summary').text
        url = IndeedJobFormatter._job_page_url(job)
        try:
            with urllib.request.urlopen(url) as u:
                page_source = u.read()
        except ValueError:
            return '&nbsp;'
        soup = BeautifulSoup(page_source, 'html.parser')
        description = soup.find('div', class_='jobsearch-JobComponent-description')
        if description is None:
            return '&nbsp;'
        # else:
        #     divs = description.find_all('div')
        #     if divs.__len__() >= 3:
        #         description = divs[2]
        out += str(description) + '</div>'
        return out

    @staticmethod
    def _location(job):
        span_tag = job.find('span', class_='location')
        if span_tag is None:
            return '&nbsp;'
        else:
            return str(span_tag.contents[0])

    @staticmethod
    def _salary(job):
        span_tag = job.find('span', class_='salary')
        if span_tag is None:
            return 'unknown'
        else:
            return str(span_tag.contents[0])

    @staticmethod
    def _date_posted(job):
        span_tag = job.find('span', class_='date')
        if span_tag is None:
            return '&nbsp;'
        else:
            return str(span_tag.contents[0])
