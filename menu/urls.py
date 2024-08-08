from django.urls import path, re_path
from django.views.generic import DetailView, TemplateView

from .views import home

urlpatterns = [
    # re_path(r'', home, name='home'),
    re_path(r'', TemplateView.as_view(template_name='menu/home.html'), name='home'),

]
