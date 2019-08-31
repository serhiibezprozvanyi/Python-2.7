#-* coding:utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.loader.processors import TakeFirst
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import XPathItemLoader
from scrapy.selector import HtmlXPathSelector
from tours.items import ToursItem


class ToursLoader(ItemLoader):
	default_output_processor = TakeFirst()

class ToursSpider(CrawlSpider):
	name = "tours"
	allowed_domains = ["tours.ua"]
	start_urls = ["http://tours.ua/agency/all"]
	rules = (
		Rule(LinkExtractor(allow=('agency/all/region/\d?page=\d')), follow=True),
		Rule(LinkExtractor(allow=('agency/all?page=\d')), follow=True),
		Rule(LinkExtractor(allow=('agency/all/region/\d')), follow=True),
		Rule(LinkExtractor(allow=('agency/\d')), callback='parse_item'),
		)
	def parse_item(self, response):
		hxs = HtmlXPathSelector(response)
		l = ToursLoader(ToursItem(), hxs)
			
		l.add_xpath('name', '//h1/text()[1]')
		#l.add_xpath('adresss', '//div[@class="agency-office"]/text()[1]')
		l.add_xpath('milo', '//div[@class="agency-office"]/b[text() = "Email:"]/following-sibling::text()[1]')
		l.add_xpath('telefon', '//div[@class="agency-office"]/b[text() = "%s"]/following-sibling::text()' % u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d\u044b:" )
		return l.load_item()