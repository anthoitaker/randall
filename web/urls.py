from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view()),
    path('version', views.Version.as_view()),
]
