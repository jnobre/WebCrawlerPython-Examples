# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider 	 import BaseSpider
from scrapy.selector import Selector

class RedeexpressoSpider(scrapy.Spider):
    name = "RedeExpresso"
    allowed_domains = ["rede-expressos.pt"]
    start_urls = (
        'http://www.rede-expressos.pt/',
    )

    def parse(self, response):
    #    filename = response.url.split("/")[-2]
     #   open(filename, 'wb').write(response.body)
     	print response
        sel = Selector(response)
        sites = sel.xpath('//a')
        for site in sites:
            title = site.xpath('a/text()').extract()
            link = site.xpath('@href').extract()
            desc = site.xpath('text()').extract()
            print title, link, desc
		#return items
