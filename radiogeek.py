#"https://jadi.net/audio/"

from BeautifulSoup import BeautifulSoup
import urllib2
import re

url = "https://jadi.net/audio/"
html_page = urllib2.urlopen(url)
soup = BeautifulSoup(html_page)
 
for link in soup.findAll('a'):
    print(url+str(link.get('href')))

