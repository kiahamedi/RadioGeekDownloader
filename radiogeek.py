#"https://jadi.net/audio/"

from bs4 import BeautifulSoup
import requests

url = "https://jadi.net/audio/"
html_page = requests.get(url)
soup = BeautifulSoup(html_page.content,'html5lib')
 
for link in soup.findAll('a'):
    print(url+str(link.get('href')))

