import requests as req
from bs4 import BeautifulSoup
import fake_useragent
from pprint import pprint

find = 'something'

user = fake_useragent.UserAgent().random
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'}
link = f'https://r501.kujo-jotaro.com/kaiji/1/2.480.022a69705bdc85de.mp4?hash1=268cb054e6bfeba531dce35291f37f56'
print()

resp = req.get(link, headers=header).text
soup = BeautifulSoup(resp, 'html.parser')

content = soup.find('div', class_='border_around_video')
pprint(content)
