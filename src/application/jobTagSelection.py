from bs4 import BeautifulSoup

class JobTagSelection:
    @classmethod
    def select(cls, job):
        out = "<div class='job'>"
        out += str(job.find('div', class_='job-title')).replace('<a ', '<a target="_blank" rel="noopener noreferrer" ')
        out += str(job.find('p', class_='job-intro'))
        out += "</div>"
        return out.replace('...', "").replace('…',"").replace('  ', ' ').replace(" ", ' ')

