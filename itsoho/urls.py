# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^jsi18n/', 'django.views.i18n.javascript_catalog'),
    url(r'^auth/', include('itsoho.core.auth.urls')),
    url(r'^charge/', include('itsoho.core.charge.urls')),
    url(r'^manage/', include('itsoho.core.manage.urls')),
    url(r'', include('itsoho.core.home.urls')),
)


from django.conf import settings

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns
