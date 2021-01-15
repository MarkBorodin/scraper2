import random
import uuid

import scrapy
from bs4 import BeautifulSoup
from scrapy_splash import SplashRequest

from test_scraper.items import TestScraperItem


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['sos-kinderdorf.ch']
    start_urls = ['http://sos-kinderdorf.ch/']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 5.0})

    def parse(self, response, **kwargs):
        item = TestScraperItem()
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        item['uuid'] = str(uuid.uuid1())
        item['url'] = self.start_urls[0]
        item['site_title'] = str(soup.title.string)
        item['meta_description'] = str(soup.find('head').find_all('meta'))
        item['html_lang'] = str(soup.find('html').get('lang'))
        item['a_href'] = str([href.get('href') for href in soup.find_all('a')])
        item['a'] = str(soup.find_all('a'))
        item['alt'] = str([alt.get('alt') for alt in soup.find_all('img')])
        item['h1'] = str([h1.text.strip() for h1 in soup.find_all('h1')])
        item['h2'] = str([h2.text.strip() for h2 in soup.find_all('h2')])
        item['h3'] = str([h3.text.strip() for h3 in soup.find_all('h3')])
        item['h4'] = str([h4.text.strip() for h4 in soup.find_all('h4')])
        item['h5'] = str([h5.text.strip() for h5 in soup.find_all('h5')])
        item['p'] = str([p.text.strip() for p in soup.find_all('p')])
        item['score'] = str(random.randint(1, 101))
        item['department'] = str(random.choice(['Government', 'School', 'Non-Profit', 'Marketing', 'Development']))
        print(item)
        return item
