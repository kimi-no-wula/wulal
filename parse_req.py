import requests as req
from bs4 import BeautifulSoup
from pprint import pprint

find = 'something'
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'}
link = f'https://azbyka.ru/fiction/sobache-serdce-bulgakov/'
print()

resp = req.get(link, headers=header).text
soup = BeautifulSoup(resp, 'html.parser')

content = soup.find('div', class_='article-single-content main-page-content').get_text()
pprint(content)

