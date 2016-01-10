from django.conf.urls import patterns, url, include
from datetime import datetime

from . import views

urlpatterns = [
    url(r'^$', views.medoc, name='medoc'),
    url(r'^auth_login/$', views.auth_login, name="auth_login"),
    url(r'^register/$', views.auth_register, name="register")
]