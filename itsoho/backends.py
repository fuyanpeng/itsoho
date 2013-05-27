# -*- coding: utf-8 -*-
from django.contrib.auth.backends import ModelBackend
from itsoho.core.auth.models import Xuser as User

class EmailOrUsernameModelBackend(ModelBackend):

    def authenticate(self, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
