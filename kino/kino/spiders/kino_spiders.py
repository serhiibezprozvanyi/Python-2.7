#-* coding:utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.loader.processors import TakeFirst
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import XPathItemLoader
from scrapy.selector import HtmlXPathSelector
from kino.items import KinoItem


class KinoLoader(ItemLoader):
	default_output_processor = TakeFirst()

class KinoSpider(CrawlSpider):
	name = "kino"
	allowed_domains = ["my-hit.org"]
	start_urls = ["https://my-hit.org/film/"]
	rules = (
		Rule(LinkExtractor(allow=('film/\?p=\d')), follow=True),
		Rule(LinkExtractor(allow=('film/\d')), callback='parse_item'),
		)
	def parse_item(self, response):
		hxs = HtmlXPathSelector(response)
		l = KinoLoader(KinoItem(), hxs)
			
		l.add_xpath('name', '//h1/text()[1]')
		l.add_xpath('nameang', '//h4/text()')
		#l.add_xpath('datafilm', '//h1/a/text()')
		l.add_xpath('dlina', '//div[@class="col-xs-10 col-md-8"]/ul[@class="list-unstyled"]/li/b[text()[1] = "%s"]/following-sibling::text()' % u"\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c:" )
		l.add_xpath('genre', '//div[@class="col-xs-10 col-md-8"]/ul[@class="list-unstyled"]/li/b[text()[1] = "%s"]/following-sibling::a/text()' % u"\u0416\u0430\u043d\u0440:" )
		l.add_xpath('strana', '//div[@class="col-xs-10 col-md-8"]/ul[@class="list-unstyled"]/li/b[text()[1] = "%s"]/following-sibling::a/text()' % u"\u0421\u0442\u0440\u0430\u043d\u0430:" )
		l.add_xpath('rezhisser', '//div[@class="col-xs-10 col-md-8"]/ul[@class="list-unstyled"]/li/b[text()[1] = "%s"]/following-sibling::a/text()' % u"\u0420\u0435\u0436\u0438\u0441\u0441\u0435\u0440:" )
		l.add_xpath('scenari', '//div[@class="col-xs-10 col-md-8"]/ul[@class="list-unstyled"]/li/b[text()[1] = "%s"]/following-sibling::a/text()' % u"\u0421\u0446\u0435\u043d\u0430\u0440\u0438\u0439:" )
		l.add_xpath('foto', '//div/img[@class="img-rounded img-responsive"]/@src')
		#l.add_xpath('slogan', '//div[@class="col-xs-10 col-md-8"]/ul[@class="list-unstyled"]/li[4]/text()')
		
		
			
		return l.load_item()
		
		