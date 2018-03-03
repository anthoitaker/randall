import scrapy


class DtcSpider(scrapy.Spider):
    name = "codigosdtc"

    def start_requests(self):
        urls = ['https://codigosdtc.com/p0303/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        code = response.url.split("/")[-2]
        filename = 'codigosdtc-%s.html' % code

        with open(filename, 'wb') as f:
            f.write(response.body)

        self.log('Saved file %s' % filename)
