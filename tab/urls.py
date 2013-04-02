<<<<<<< HEAD
from django.conf.urls import patterns, url

from tab import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
)
=======
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

import views

urlpatterns = patterns('',
    url(r'^charts', views.grafi),
    url(r'^users', views.uporabniki),
    url(r'^', views.index),
)
>>>>>>> e7629dc5cac9a546e20c5cb4714e1db24fff720a
