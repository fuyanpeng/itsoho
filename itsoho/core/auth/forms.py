# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate
from django.db.models import Q
from django.contrib.admin.widgets import AdminDateWidget
from django.utils.translation import ugettext_lazy as _

from itsoho.core.auth.models import Xuser as User, BaseInfo, EduInfo


class XuserForm(forms.ModelForm):

    class Meta:
        model = User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(label=_(u'记住登录'),
                                     initial=True,
                                     required=False,
                                     widget=forms.CheckboxInput)
    next = forms.CharField(widget=forms.HiddenInput, required=False)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].error_messages['required'] =  u"请输入用户名"
        self.fields['password'].error_messages['required'] =  u"请输入密码"

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not User.objects.filter(Q(username=username)|Q(email=username)).exists():
            self._errors['username'] = self.error_class([u"该用户不存在。",])

        return username

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if User.objects.filter(Q(username=username)|Q(email=username)).exists():
            self._user = authenticate(username=username, password=password)
            if self._user is None:
                self._errors['password'] = self.error_class([u'密码错误。',])
        return password

    def get_user(self):
        return self._user


class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].error_messages['required'] =  u"请输入用户名"
        self.fields['email'].error_messages['invalid'] =  u"邮箱格式不正确"
        self.fields['password'].error_messages['required'] =  u"请输入密码"


class BaseInfoForm(forms.ModelForm):

    class Meta:
        model = BaseInfo
        exclude = ('user',)
        widgets = {
            'birthday': AdminDateWidget(),
        }


class EduInfoForm(forms.ModelForm):

    class Meta:
        model = EduInfo
        exclude = ('user',)
