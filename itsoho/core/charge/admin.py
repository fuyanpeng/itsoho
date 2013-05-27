# -*- coding: utf-8 -*-
from django.contrib import admin
from itsoho.core.charge.models import Category, Entry, Tag, Comment

admin.site.register(Category)
admin.site.register(Entry)
admin.site.register(Tag)
admin.site.register(Comment)

