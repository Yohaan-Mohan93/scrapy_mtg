import scrapy
from scrapy_playwright.page import PageCoroutine


class CardSpiderSpider(scrapy.Spider):
    name = 'card_spider'

    def start_requests(self):
        yield scrapy.Request('https://www.cardkingdom.com/mtg/alpha',
                             meta =  dict(
                                 playwright=True,
                                 playwright_include_page=True,
                                 playwright_page_coroutines=[
                                     PageCoroutine('wait_for_selector','img.cardSrc')
                                 ]
                             ))

    def parse(self, response):
        pass
