
# # scrap all lamps from the website: name, price, link
#
# import scrapy
#
# class DivannewparsSpider(scrapy.Spider):
#     name = "divannewpars"
#     allowed_domains = ["divan.ru"]
#     start_urls = ["https://www.divan.ru/category/svet"]
#
#     def parse(self, response):
#         lamps = response.css('div.X68VV')
#         for lamp in lamps:
#             yield {
#                 'name' : lamp.css('div.LsooF  span::text').get(),
#                 'price' : lamp.css('div.pY3d2  span::text').get(),
#                 'url' : response.urljoin(lamp.css('a::attr(href)').get())
#
#             }
# spiders/divannewpars.py
import scrapy
from scrapy_playwright.page import PageCoroutine


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    async def parse(self, response):
        # теперь страница уже полностью отрендерена
        lamps = response.css('div.lsooF_1X span::text').getall()
        print(f"DEBUG: нашлось {len(lamps)} карточек")

        items = response.css('div.X68VV')
        for lamp in items:
            yield {
                'name': lamp.css('div.LsooF span::text').get(),
                'price': lamp.css('div.pY3d2 span::text').get(),
                'url': response.urljoin(lamp.css('a::attr(href)').get())
            }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                meta={
                    "playwright": True,
                    "playwright_page_coroutines": [
                        PageCoroutine("wait_for_selector", "div.X68VV")
                    ],
                           },
            )
