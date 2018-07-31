from django.http import Http404
from core.models import Trouble

def get_trouble_or_404(code):
    try:
        return Trouble.get_trouble(code=code)
    except Trouble.DoesNotExist:
        raise Http404
