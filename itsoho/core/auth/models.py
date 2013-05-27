# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

GENDER_CHOICES = (
    ('M', _(u"男")),
    ('F', _(u"女")),
    ('N', _(u"保密")),
)

VISIBLE_CHOICES = (
    ('1', _(u"所有人可见")),
    ('2', _(u"仅自己可见")),
)

DEGREE_CHOICES = (
    ('A', _(u"高中/中专")),
    ('B', _(u"大专")),
    ('C', _(u"本科")),
    ('D', _(u"硕士")),
    ('E', _(u"博士")),
    ('F', _(u"其他")),
)

class Xuser(AbstractUser):
    avatar = models.ImageField(upload_to="avatar/", blank=True, null=True, verbose_name=_(u"头像"))

    REQUIRED_FIRLDS = ['email',]

    class Meta:
        verbose_name = _(u"用户")
        verbose_name_plural = _(u"用户")

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url


class BaseInfo(models.Model):
    user = models.ForeignKey(Xuser, verbose_name=_(u"用户"))
    truename = models.CharField(max_length=128, verbose_name=_(u"真实姓名"))
    truename_visible = models.CharField(max_length=1, default='1',\
            choices=VISIBLE_CHOICES, verbose_name=_(u"可见性"))
    nickname = models.CharField(max_length=128, verbose_name=_(u"昵称"))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name=_(u"性别"))
    birthday = models.DateField(verbose_name=_(u"出生日期"))
    birthday_visible = models.CharField(max_length=1, default='1',\
            choices=VISIBLE_CHOICES, verbose_name=_(u"可见性"))
    intro = models.TextField(verbose_name=_(u"简介"))

    class Meta:
        verbose_name = _(u"基本资料")
        verbose_name_plural = _(u"基本资料")

    def __unicode__(self):
        return self.user.username

    @property
    def get_truename_display(self):
        if self.truename_visible == '1':
            return self.truename
        return '******'

    @property
    def get_birthday_display(self):
        if self.birthday_visible == '1':
            return self.birthday
        return '******'


class EduInfo(models.Model):
    user = models.ForeignKey(Xuser, verbose_name=_(u"用户"))
    degree = models.CharField(max_length=1, choices=DEGREE_CHOICES, verbose_name=_(u"学历"))
    name = models.CharField(max_length=255, verbose_name=_(u"学校名称"))
    major = models.CharField(max_length=255, verbose_name=_(u"专业"))
    start_time = models.DateField(verbose_name=_(u"开始时间"))
    end_time = models.DateField(verbose_name=_(u"结束时间"))

    class Meta:
        verbose_name = _(u"教育经历")
        verbose_name_plural = _(u"教育经历")
        ordering = ("degree",)

    def __unicode__(self):
        return u'%s--%s' % (self.user.username, self.get_degree_display())
