from django.urls import re_path
from . import views
urlpatterns = [
    re_path('^index/$', views.index),
    re_path('^res/$', views.get_values),
    # re_path('weather/([a-z]+)/(\d{4})/$', views.weather),
    re_path('weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather),
    re_path('^form/$', views.get_data),
]