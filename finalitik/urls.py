from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
<<<<<<< HEAD
                       url(r'^tab/', include('tab.urls')),
                       url(r'^admin/', include(admin.site.urls)),
=======
    # Examples:
    #url(r'^$', 'finalitik.views.home', name='home'),
    #url(r'^finalitik/', include('finalitik.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('tab.urls')),
>>>>>>> e7629dc5cac9a546e20c5cb4714e1db24fff720a
)
