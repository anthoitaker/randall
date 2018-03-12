import os
from django.core.management import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scraper.scraper.spiders.dtc_spider import DtcSpider
from config.settings import SCRAPY_SETTINGS_MODULE


class Command(BaseCommand):
    help = "Imports trouble from specific code"

    def add_arguments(self, parser):
        parser.add_argument('code', type=str, help='The trouble code')

    def handle(self, *args, **options):
        code = options['code']
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', SCRAPY_SETTINGS_MODULE)
        process = CrawlerProcess(get_project_settings())
        process.crawl(DtcSpider, code=code)
        process.start()
