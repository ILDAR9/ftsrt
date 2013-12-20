# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns
from django.conf.urls import url

urlpatterns = patterns('',
                       url(r'^$', 'picasagallery.views.gallery', name='photo-gallery'),
                       url(r'^album/(?P<album_id>\d+)/$', 'picasagallery.views.album_list', name='album'),
                       )
