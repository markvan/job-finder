import urllib.request
from bs4 import BeautifulSoup

with urllib.request.urlopen("https://www.cwjobs.co.uk/jobs/contract/innovation/in-london?postedwithin=1") as url:
    s = url.read()
    print(s)

soup = BeautifulSoup(s, 'html.parser')

out = ""

for link in soup.find('div', class_="job-results").find_all('div', class_="job new "):
    out += str(link.find('a'))
    out += str(link.find('p', class_="job-intro"))

print(out)
