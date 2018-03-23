from django.core.management import BaseCommand
from scraper.scraper.utils import import_trouble


class Command(BaseCommand):
    help = "Imports trouble from specific code"

    def add_arguments(self, parser):
        parser.add_argument('code', type=str, help='The trouble code')

    def handle(self, *args, **options):
        code = options['code']
        import_trouble(code)
