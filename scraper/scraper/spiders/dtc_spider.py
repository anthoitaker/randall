import scrapy


class DtcSpider(scrapy.Spider):
    name = "codigosdtc"
    start_urls = ['https://codigosdtc.com/p0303/']

    def parse(self, response):
        code = response.url.split("/")[-2]
        filename = 'codigosdtc-%s.html' % code

        with open(filename, 'wb') as f:
            f.write(response.body)

        self.log('Saved file %s' % filename)
