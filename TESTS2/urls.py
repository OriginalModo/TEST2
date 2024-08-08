from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('', include('menu.urls')),
]
