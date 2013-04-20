#-*- coding:utf-8 -*-

from nscms.base.db.models import SimpleContentModel, \
    PublisherModel

from django.db import models
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey
from tinymce.models import HTMLField


class SimplePageModel(MPTTModel, SimpleContentModel, PublisherModel):
    parent = TreeForeignKey(
        'self', verbose_name=_(u"Pai"), null=True, blank=True,
        related_name='children')
    content = HTMLField(blank=True)
    redirect_to = TreeForeignKey(
        'self', verbose_name=_(u"Redirecionar para página"),
        null=True, blank=True,
        related_name='redirected_from')
    redirect_to_url = models.URLField(
        verbose_name=_(u"Redirecionar para esta URL"), blank=True)

    class Meta:
        abstract = True
