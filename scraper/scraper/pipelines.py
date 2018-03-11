# -*- coding: utf-8 -*-

import re

class CleanDataPipeline(object):
    TAG_RE = re.compile(r'<[^>]+>')
    NON_BREAK_SPACE = u'\xa0'

    def process_item(self, item, spider):
        item['code'] = self._clean_code(item['code'])
        item['title'] = self._clean_title(item['title'])
        item['original_title'] = self._clean_title(item['original_title'])
        item['system'] = self._clean_system(item['system']) if item['system'] else None
        item['description'] = self._clean_description(item['description'])
        item['symptoms'] = self._clean_text_list(item['symptoms'])
        item['causes'] = self._clean_text_list(item['causes'])
        item['solutions'] = self._clean_text_list(item['solutions'])
        return item

    def _clean_code(self, code):
        clean_code = self._clean_text(code)
        clean_code = clean_code.upper()
        return clean_code

    def _clean_title(self, title):
        clean_title = self._clean_text(title)
        clean_title = clean_title.split('-', 1)[1].strip().capitalize()
        return clean_title

    def _clean_system(self, system):
        clean_system = self._clean_text(system)
        clean_system = clean_system.capitalize()
        return clean_system

    def _clean_description(self, description):
        description = '\n'.join(description)
        clean_description = self._clean_text(description, dot=True)
        return clean_description

    def _clean_text(self, text, dot=False):
        text = self.TAG_RE.sub('', text)
        text = text.replace(self.NON_BREAK_SPACE, ' ')
        clean_text = re.sub(' +', ' ', text)
        clean_text = clean_text + '.' if dot and clean_text[-1] != '.' else clean_text
        return clean_text

    def _clean_text_list(self, text_list):
        return [self._clean_text(text, dot=True) for text in text_list]
