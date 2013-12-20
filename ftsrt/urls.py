from django.conf.urls import patterns, include, url
from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', direct_to_template, {'template': 'home.html'}),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^news/', include('easy_news.urls')),
                       url(r'^accounts/profile', lambda x: HttpResponseRedirect('/')),
                       url(r'^accounts/', include('registration.urls')),
                       url(r'^administration/', include('administration.urls')),
                       url(r'^forum/', include('pybb.urls', namespace='pybb')),
                       url(r'^404/$', direct_to_template, {'template': '404.html'}),
                       url(r'^grappelli/', include('grappelli.urls')),
                       url(r'^photo-gallery/', include('picasagallery.urls')),
                       url(r'^', include('cms.urls'))
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': settings.STATIC_ROOT}),
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

    )
