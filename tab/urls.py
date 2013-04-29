from django.conf.urls import patterns, url, include

from tastypie.api import Api
from tab.resources import TabResource
from tab import views

v1_api = Api(api_name='v1')
v1_api.register(TabResource())

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^api/', include(v1_api.urls)),
)
