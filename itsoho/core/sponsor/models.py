#! -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Sponsor(models.Model):
    name = models.CharField(max_length=128, verbose_name=_(u"名称"))
    cover = models.ImageField(upload_to="sponsor/", verbose_name=_(u"封面"))
    url = models.URLField(verbose_name=_(u"网址"))
    worth = models.IntegerField(blank=True, null=True, verbose_name=_(u"价值"))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _(u"赞助商")
        verbose_name_plural = _(u"赞助商")
        ordering = ("worth", "-created_at")

    def __unicode__(self):
        return self.name

    def get_cover_url(self):
        if self.cover:
            return self.cover.url

