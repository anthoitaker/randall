from django.urls import path, re_path
from . import views

DTC_PARAM = '(?P<dtc>[a-zA-Z0-9]{5})'

urlpatterns = [
    path('troubles/', views.TroubleList.as_view(), name='list-troubles'),
    re_path(r'^troubles/{}/$'.format(DTC_PARAM), views.TroubleDetail.as_view(), name='get-trouble'),
    path('systems/', views.SystemList.as_view(), name='list-systems'),
    re_path(r'^troubles/{}/symptoms/$'.format(DTC_PARAM), views.SymptomList.as_view(), name='list-symptoms'),
    re_path(r'^troubles/{}/causes/$'.format(DTC_PARAM), views.CauseList.as_view(), name='list-causes'),
    re_path(r'^troubles/{}/solutions/$'.format(DTC_PARAM), views.SolutionList.as_view(), name='list-solutions'),
]
