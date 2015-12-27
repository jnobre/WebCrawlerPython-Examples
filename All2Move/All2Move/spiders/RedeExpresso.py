# -*- coding: utf-8 -*-
import scrapy


class RedeexpressoSpider(scrapy.Spider):
    name = "RedeExpresso"
    allowed_domains = ["http://www.rede-expressos.pt/"]
    start_urls = (
        'http://www.http://www.rede-expressos.pt//',
    )

    def parse(self, response):
        pass
