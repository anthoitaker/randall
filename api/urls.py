from django.urls import path, re_path
from . import views

DTC_PARAM = '(?P<dtc>[a-zA-Z0-9]{5})'

urlpatterns = [
    path('troubles/', views.TroubleList.as_view(), name='list-troubles'),
    re_path(r'^troubles/{}/$'.format(DTC_PARAM), views.TroubleDetail.as_view(), name='get-trouble'),
]
