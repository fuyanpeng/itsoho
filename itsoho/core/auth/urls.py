# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('itsoho.core.auth.views',

    url('^login/$','login', name='auth_login'),
    url('^logout/$','logout', name='auth_logout'),
    url('^register/$','register', name='auth_register'),

)
