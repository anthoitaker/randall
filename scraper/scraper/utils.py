import os
import scrapydo
from scrapy.utils.project import get_project_settings
from scraper.scraper.spiders.dtc_spider import DtcSpider
from config.settings import SCRAPY_SETTINGS_MODULE


scrapydo.setup()

def import_trouble(code):
    os.environ.setdefault('SCRAPY_SETTINGS_MODULE', SCRAPY_SETTINGS_MODULE)
    scraper_settings = get_project_settings()
    scrapydo.run_spider(DtcSpider, settings=scraper_settings, code=code)
