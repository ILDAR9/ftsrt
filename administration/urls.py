# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf.urls.defaults import patterns
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
                       url(r'^$', 'administration.views.get_administration', name='director'),
                       url(r'^info$', direct_to_template, {'template': 'administration/about.html'}, name='info'),
                       url(r'^docs$', 'administration.views.get_docs', name='docs'),
                       url(r'^tournaments$', 'administration.views.get_tournaments', name='tournaments'),
                       url(r'^clubs$', 'administration.views.get_clubs', name='clubs'),
                       url(r'^club/(?P<dance_club_id>\d+)/$', 'administration.views.club_detail', name='club'),
                       url(r'^coach/(?P<coach_id>\d+)/$', 'administration.views.get_coach', name='coach'),
                       url(r'^any-club', 'administration.views.any_club', name='any-club'),
                       url(r'^load-file$', 'administration.views.load_file', name='load_file')
)
