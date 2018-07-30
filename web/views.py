from django.http import HttpResponse
from django.views import View
import markdown2


class Home(View):
    README_PATH = 'README.md'

    def get(self, request):
        with open(self.README_PATH) as readme_file:
            readme_content = readme_file.read()
            readme_html = markdown2.markdown(readme_content, extras=['tables'])
            return HttpResponse(readme_html)


class Version(View):
    VERSION_PATH = 'version.txt'

    def get(self, request):
        with open(self.VERSION_PATH) as version_file:
            version = version_file.read()
            return HttpResponse(version)
