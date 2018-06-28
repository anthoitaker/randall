from django.contrib import admin
from django.views.static import serve
from django.urls import path, re_path, include
from .settings import STATIC_ROOT

urlpatterns = [
    path('', include('web.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^static/(.*)$', serve, {
        'document_root': STATIC_ROOT,
    }),
]
