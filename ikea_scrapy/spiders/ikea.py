# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:34:43 2024

@author: vilok
"""

import scrapy
class Ikea(scrapy.Spider):
    name = 'ikea'
    start_urls = ['https://www.ikea.com/in/en/cat/lower-price/']
    def parse(self, response):
        for product in response.css('.plp-price-module'):
            name = product.css('.plp-price-module__product-name::text').get()
            description = product.css('.plp-price-module__description::text').get()
            price = product.css('.plp-price-module__current-price .plp-price__integer::text').get()
            yield{
                'name': name.strip(),
                'descri': description.strip(),
                'price': f"Rs. {price}"
                #'name': product.css('.plp-price-module__product-name::text').get(),strip(),
                #'descri':product.css('.plp-price-module__description::text').get(),
                #'price': product.css('.plp-price__sr-text::text').get(),
                }
        next_page = response.css('.plp-btn--secondary::attr(href)').get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)