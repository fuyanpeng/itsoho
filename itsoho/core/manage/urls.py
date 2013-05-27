# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('itsoho.core.manage.views',
    url(r'^$', 'manage_home', name='manage_home'),
    url(r'^private/$', 'manage_baseinfo', name='manage_baseinfo'),
    url(r'^private/edu/$', 'manage_eduinfo', name='manage_eduinfo'),
)
