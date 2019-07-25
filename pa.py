# -*- coding: utf-8 -*-
import scrapy


class PaSpider(scrapy.Spider):
    name = 'pa'
    allowed_domains = ['https://www.zhaopin.com/']
    start_urls = ['http://https://www.zhaopin.com//']

    def parse(self, response):
        pass
