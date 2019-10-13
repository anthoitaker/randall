import scrapy
from scrapy.loader import ItemLoader
from scraper.scraper.items import TroubleItem


class DtcSpider(scrapy.Spider):
    name = 'codigosdtc'

    def __init__(self, code=None, *args, **kwargs):
        super(DtcSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://codigosdtc.com/{}/'.format(code)]

    def parse(self, response):
        loader = ItemLoader(item=TroubleItem(), response=response)
        loader.add_value('code', response.url.split('/')[-2])
        loader.add_css('title', 'div.position-relative h1::text')
        loader.add_css('original_title', 'div.meta-title-single span::text')
        loader.add_css('system', 'span span.color-red::text')
        loader.add_value('description', self._extract_description(response))
        loader.add_value('symptoms', self._extract_symptoms(response))
        loader.add_value('causes', self._extract_causes(response))
        loader.add_value('solutions', self._extract_solutions(response))
        return loader.load_item()

    def _extract_description(self, response):
        paragraphs = response.css('div.position-relative div.text-content')[0]
        paragraphs_list = paragraphs.css('p').extract()
        return paragraphs_list

    def _extract_symptoms(self, response):
        symptoms = response.css('div.position-relative div.text-content')[1]
        symptoms_list = symptoms.css('ul li').extract()
        return symptoms_list

    def _extract_causes(self, response):
        causes = response.css('div.position-relative div.text-content')[2]
        causes_list = causes.css('ul li').extract()
        return causes_list

    def _extract_solutions(self, response):
        solutions = response.css('div.position-relative div.text-content')[3]
        solutions_list = solutions.css('ul li').extract()
        return solutions_list
