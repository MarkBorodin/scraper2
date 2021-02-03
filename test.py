import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.sos-kinderdorf.ch/')
html = r.text
soup = BeautifulSoup(html, 'lxml')
# print(html)
m = soup.find('p')

print(f'!!!!!!!!!!!!!!!!{m}!!!!!!!!!!!!!!!!!!')
