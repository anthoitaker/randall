import scrapy
from scrapy.loader import ItemLoader
from scraper.items import TroubleItem


class DtcSpider(scrapy.Spider):
    name = 'codigosdtc'

    def __init__(self, code=None, *args, **kwargs):
        super(DtcSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://codigosdtc.com/{}/'.format(code)]

    def parse(self, response):
        loader = ItemLoader(item=TroubleItem(), response=response)
        loader.add_value('code', response.url.split('/')[-2])
        loader.add_css('title', 'h1.title-single2::text')
        loader.add_css('original_title', 'div.nivel::text')
        loader.add_css('system', 'span.level::text')
        loader.add_css('description', 'div.text p')
        loader.add_value('symptoms', self._extract_symptoms(response))
        loader.add_value('causes', self._extract_causes(response))
        loader.add_value('solutions', self._extract_solutions(response))
        return loader.load_item()

    def _extract_symptoms(self, response):
        symptoms = response.css('div.text1')[0]
        symptoms_list = symptoms.css('ul li').extract()
        return symptoms_list

    def _extract_causes(self, response):
        causes = response.css('div.text1')[1]
        causes_list = causes.css('ul li').extract()
        return causes_list

    def _extract_solutions(self, response):
        solutions = response.css('div.text1')[2]
        solutions_list = solutions.css('ul li').extract()
        return solutions_list
