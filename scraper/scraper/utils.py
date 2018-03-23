import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scraper.scraper.spiders.dtc_spider import DtcSpider
from config.settings import SCRAPY_SETTINGS_MODULE


def import_trouble(code):
    os.environ.setdefault('SCRAPY_SETTINGS_MODULE', SCRAPY_SETTINGS_MODULE)
    process = CrawlerProcess(get_project_settings())
    process.crawl(DtcSpider, code=code)
    process.start()
