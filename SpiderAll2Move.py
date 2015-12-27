#!/usr/bin/env python
#
# Hi There!
# Spider analyzes sites pulling out information about used routes 

import scrapy




if __name__ == '__main__':
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]