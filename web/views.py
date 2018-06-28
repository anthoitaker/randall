from django.http import HttpResponse
from django.views import View


class Home(View):
    def get(self, request):
        return HttpResponse('<h1>randall</h1>')


class Version(View):
    VERSION_PATH = 'version.txt'
  
    def get(self, request):
        with open(self.VERSION_PATH) as f:
            version = f.read()
            return HttpResponse(version)
