
# scrap all lamps from the website: name, price, link

import scrapy

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        lamps = response.css('div.X68VV')
        for lamp in lamps:
            yield {
                'name' : lamp.css('div.LsooF  span::text').get(),
                'price' : lamp.css('div.pY3d2  span::text').get(),
                'url' : response.urljoin(lamp.css('a::attr(href)').get())

            }
