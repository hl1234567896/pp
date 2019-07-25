# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item): # Item类型
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name=scrapy.Field()
    job_message=scrapy.Field()
    company_name=scrapy.Field()
    company_information=scrapy.Field()
    good=scrapy.Field()
















