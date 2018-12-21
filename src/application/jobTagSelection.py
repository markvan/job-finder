from bs4 import BeautifulSoup


class JobTagSelection:
    @classmethod
    def select(cls, job):
        out = ""
        out += str(job.find('div', class_='job-title'))
        out += str(job.find('p', class_='job-intro'))
        return out.replace('...', "").replace('…',"").replace('  ', ' ').replace(" ", ' ')

