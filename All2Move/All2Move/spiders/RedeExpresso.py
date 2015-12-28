# -*- coding: utf-8 -*-
import scrapy


class RedeexpressoSpider(scrapy.Spider):
    name = "RedeExpresso"
    allowed_domains = ["rede-expressos.pt"]
    start_urls = (
        'http://www.rede-expressos.pt/',
    )

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)
