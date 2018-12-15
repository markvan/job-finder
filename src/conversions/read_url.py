import urllib.request
from bs4 import BeautifulSoup

with urllib.request.urlopen("http://www.python.org") as url:
    s = url.read()
    print(s)

soup = BeautifulSoup(s, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
