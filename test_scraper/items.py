# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TestScraperItem(scrapy.Item):
    uuid = scrapy.Field()
    url = scrapy.Field()
    site_title = scrapy.Field()
    meta_description = scrapy.Field()
    html_lang = scrapy.Field()
    a_href = scrapy.Field()
    a = scrapy.Field()
    alt = scrapy.Field()
    h1 = scrapy.Field()
    h2 = scrapy.Field()
    h3 = scrapy.Field()
    h4 = scrapy.Field()
    h5 = scrapy.Field()
    p = scrapy.Field()
    score = scrapy.Field()
    department = scrapy.Field()
