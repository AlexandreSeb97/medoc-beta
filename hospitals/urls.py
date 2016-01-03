from django.conf.urls import patterns, url, include
from datetime import datetime

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hospital$', views.hospital, name='hospital'),
    url(r'^hospital_fr$', views.hospital_fr, name='hospital_fr'),
    url(r'^hospital_kr$', views.hospital_kr, name='hospital_kr'),
]
