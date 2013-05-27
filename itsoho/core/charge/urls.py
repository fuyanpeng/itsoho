# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('itsoho.core.charge.views',
    url(r'^$', 'charge_index', name='charge_index'),
    url(r'^(?P<category_id>\d+)/$', 'charge_entry_list', name='charge_entry_list'),
    url(r'^(?P<category_id>\d+)/(?P<entry_id>\d+)/(?P<entry_slug>[\w-]+)?/$',\
        'charge_entry_detail', name='charge_entry_detail'),
)
