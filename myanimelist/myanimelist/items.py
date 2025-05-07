# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyanimelistItem(scrapy.Item):
    # define the fields for your item here like:

    title = scrapy.Field()
    covers_path = scrapy.Field()
    small_cover_path = scrapy.Field()
    id = scrapy.Field()
    score = scrapy.Field()
    rank = scrapy.Field()
    status = scrapy.Field()
    episodes = scrapy.Field()
    synopsis = scrapy.Field()
    link = scrapy.Field()
    test = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    results = scrapy.Field()
