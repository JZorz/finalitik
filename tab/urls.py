from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

import views

urlpatterns = patterns('',
    url(r'^charts', views.grafi),
    url(r'^users', views.uporabniki),
    url(r'^', views.index),
)
