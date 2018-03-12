# -*- coding: utf-8 -*-

import re
from core.models import Trouble, System, Symptom, Cause, Solution


class CleanDataPipeline(object):
    TAG_RE = re.compile(r'<[^>]+>')
    NON_BREAK_SPACE = u'\xa0'

    def process_item(self, item, spider):
        item['code'] = self._clean_code(item['code'])
        item['title'] = self._clean_title(item['title'])
        item['original_title'] = self._clean_title(item['original_title'])
        item['system'] = self._clean_system(item['system']) if item.get('system') else None
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
        description = '\n\n'.join(description)
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


class StorePipeline(object):

    def process_item(self, item, spider):
        system = self._get_or_create_system(item)
        trouble = self._create_trouble(item, system)
        self._create_symptoms(item, trouble)
        self._create_causes(item, trouble)
        self._create_solutions(item, trouble)
        return item

    def _get_or_create_system(self, item):
        if item.get('system'):
            system, _ = System.objects.get_or_create(name=item['system'])
        else:
            system = None

        return system

    def _create_trouble(self, item, system):
        return Trouble.objects.create(
            code=item['code'],
            title=item['title'],
            original_title=item['original_title'],
            description=item['description'],
            system=system
        )

    def _create_symptoms(self, item, trouble):
        for symptom_desc in item['symptoms']:
            Symptom.objects.create(description=symptom_desc, trouble=trouble)

    def _create_causes(self, item, trouble):
        for cause_desc in item['causes']:
            Cause.objects.create(description=cause_desc, trouble=trouble)

    def _create_solutions(self, item, trouble):
        for solution_desc in item['solutions']:
            Solution.objects.create(description=solution_desc, trouble=trouble)
