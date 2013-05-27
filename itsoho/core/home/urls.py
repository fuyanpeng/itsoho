# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('itsoho.core.home.views',
    url(r'^$', 'home', name='home'),

)
