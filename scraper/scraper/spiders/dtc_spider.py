import re
import scrapy


class DtcSpider(scrapy.Spider):
    TAG_RE = re.compile(r'<[^>]+>')
    NON_BREAK_SPACE = u'\xa0'

    name = 'codigosdtc'
    start_urls = ['https://codigosdtc.com/p0303/']

    def parse(self, response):
        yield {
            'code': self._extract_code(response),
            'title': self._extract_title(response),
            'original_title': self._extract_original_title(response),
            'system': self._extract_system(response),
            'description': self._extract_description(response),
            'symptoms': self._extract_symptoms(response),
            'causes': self._extract_causes(response),
            'solutions': self._extract_solutions(response),
        }

    def _extract_code(self, response):
        code = response.url.split('/')[-2]
        code = code.upper()
        return code

    def _extract_title(self, response):
        title = response.css('h1.title-single2::text').extract_first()
        clean_title = title.split('-', 1)[1].strip().capitalize()
        return clean_title

    def _extract_original_title(self, response):
        original_title = response.css('div.nivel::text').extract_first()
        clean_original_title = original_title.split('-', 1)[1].strip().capitalize()
        return clean_original_title

    def _extract_system(self, response):
        system = response.css('span.level::text').extract_first()
        return system

    def _extract_description(self, response):
        paragraphs = response.css('div.text p').extract()
        description = '\n'.join(paragraphs)
        clean_description = self._clean_text(description)
        return clean_description

    def _extract_symptoms(self, response):
        symptoms = response.css('div.text1')[0]
        symptoms_list = symptoms.css('ul li').extract()
        clean_symptoms_list = [self._clean_text(symptom) for symptom in symptoms_list]
        return clean_symptoms_list

    def _extract_causes(self, response):
        causes = response.css('div.text1')[1]
        causes_list = causes.css('ul li').extract()
        clean_causes_list = [self._clean_text(cause) for cause in causes_list]
        return clean_causes_list

    def _extract_solutions(self, response):
        solutions = response.css('div.text1')[2]
        solutions_list = solutions.css('ul li').extract()
        clean_solutions_list = [self._clean_text(solution) for solution in solutions_list]
        return clean_solutions_list

    def _clean_text(self, text):
        text = self.TAG_RE.sub('', text)
        text = text.replace(self.NON_BREAK_SPACE, ' ')
        clean_text = re.sub(' +', ' ', text)
        clean_text = clean_text + '.' if clean_text[-1] != '.' else clean_text
        return clean_text
