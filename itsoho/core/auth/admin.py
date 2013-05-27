# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from itsoho.core.auth.models import Xuser, BaseInfo, EduInfo
from itsoho.core.auth.forms import XuserForm

class XuserAdmin(UserAdmin):
    model = Xuser
    form = XuserForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'avatar', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions'),
                            'classes': ['collapse']}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined'),
                                'classes': ['collapse',]}),
    )


admin.site.register(BaseInfo)
admin.site.register(EduInfo)
admin.site.register(Xuser, XuserAdmin)

