from django.conf.urls import patterns, url, include
from datetime import datetime

from . import views

urlpatterns = [
    url(r'^$', views.medoc, name='medoc'),
    url(r'^auth_login/$', views.auth_login, name="auth_login"),
    url(r'^auth_logout/$', views.auth_logout, name="auth_logout"),
    url(r'^register/$', views.auth_register, name="register"),
    url(r'^update/$', views.update_account, name="update"),
    url(r'^create/$', views.create_view, name="create"),
    url(r'^base/$', views.base, name="base"),
]