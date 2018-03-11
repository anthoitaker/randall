# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader.processors import TakeFirst


class TroubleItem(scrapy.Item):
    code = scrapy.Field(output_processor=TakeFirst())
    title = scrapy.Field(output_processor=TakeFirst())
    original_title = scrapy.Field(output_processor=TakeFirst())
    system = scrapy.Field(output_processor=TakeFirst())
    description = scrapy.Field()
    symptoms = scrapy.Field()
    causes = scrapy.Field()
    solutions = scrapy.Field()
