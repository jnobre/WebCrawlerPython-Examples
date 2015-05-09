import scrapy


from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.contrib.linkextractors import linkextractors
from imgur.items import ImgurItem


class ImgurSpider(CrawlSpider):
	name = 'imgur'
	allowed_domains = ['imgur.com']
	start_urls = ['http://www.imgur.com']
	rules = [Rule(LinkExtractor(allow=['/gallary/.*']), 'parse_imgur')]

	def parse_imgur(self, response):
		image = ImgurItem()
		image['title'] = response.xpath(\)
		
