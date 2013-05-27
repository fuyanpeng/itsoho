# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from unidecode import unidecode
from itsoho.core.auth.models import Xuser as User
import re
import random


class Category(models.Model):

    parent = models.ForeignKey('self', null=True, blank=True, verbose_name=_(u'所属分类'))
    name = models.CharField(max_length=128, verbose_name=_(u'分类名称'))
    slug = models.SlugField()
    position = models.IntegerField(null=True, blank=True, verbose_name=_(u'排序'),\
                                   help_text=u'输入整数,数字越小越靠前')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("position", "-created_at")
        verbose_name = _(u'分类')
        verbose_name_plural = _(u'分类')

    def __unicode__(self):
        return self.name

    def get_entry_count(self):
        return self.entry_set.count()

    @models.permalink
    def get_absolute_url(self):
        return 'charge_entry_list', (str(self.pk),)


class Tag(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = _(u'标签')
        verbose_name_plural = _(u'标签')

    def __unicode__(self):
        return self.name

    @property
    def size(self):
        return '%dpx' % random.randint(12, 20)

    @property
    def color(self):
        r = lambda: random.randint(0,255)
        return '#%02X%02X%02X' % (r(), r(), r())


class Entry(models.Model):
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category, verbose_name=_(u'所属分类'))
    slug = models.SlugField(blank=True)
    title = models.CharField(max_length=255,verbose_name=_(u'标题'))
    text = models.TextField(verbose_name=_(u'内容'))
    click_count = models.IntegerField(default=0, editable=False)
    tags = models.ManyToManyField(Tag, null=True, blank=True, verbose_name=_(u"标签"))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _(u'文章')
        verbose_name_plural = _(u'文章')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('charge_entry_detail',\
                       args=[self.category.id, self.id, self.slug])

    def get_summary(self):
        data = self.text
        p = re.compile(r'<.*?>')
        return p.sub('', data)[:170]

    def get_comment_count(self):
        return self.comments.count()

    @property
    def get_tags(self):
        return self.tags.all()

    @property
    def tags_name(self):
        return ",".join([x.name for x in self.tags.all()])

    def save(self, *args, **kwargs):
        if not self.slug:
            title = self.title[:8]
            self.slug = slugify(unidecode(title))

        return super(Entry, self).save(*args, **kwargs)


class Comment(models.Model):

    entry = models.ForeignKey(Entry, related_name="comments", verbose_name=_(u'文章'))
    user = models.ForeignKey(User, verbose_name=_(u"评论人"))
    content = models.TextField(verbose_name=_(u'评论'))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name = _(u'评论')
        verbose_name_plural = _(u'评论')

    def __unicode__(self):
        return u'%s--%s' % (self.user, self.content)

