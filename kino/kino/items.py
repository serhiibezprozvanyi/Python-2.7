# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KinoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    nameang = scrapy.Field()
	#datafilm = scrapy.Field()
    dlina = scrapy.Field()
    genre = scrapy.Field()
    strana = scrapy.Field()
    rezhisser = scrapy.Field()
    scenari = scrapy.Field()
    slogan = scrapy.Field()
    foto = scrapy.Field()
    pass

	