#pip install beautifulsoup
pip install requests
from bs4 import BeautifulSoup
import requests
site=requests.get('https://climatempo.com.br').content
soup=BeautifulSoup(site, 'html.parser')
temp=soup.find('span', class_='_block _margin-b-5 -gray')
print(soup.prettify())
print(soup.title.string)
print(temp.string)