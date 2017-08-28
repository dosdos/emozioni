# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from .constants import EMOTION_CATEGORIES_CHOICES, JOY


class DateTimeModel(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, db_index=True)
    last_change_date = models.DateTimeField(auto_now=True, db_index=True)

    class Meta(object):
        abstract = True


@python_2_unicode_compatible
class Emotion(DateTimeModel):
    name = models.CharField(max_length=100, db_index=True, unique=True)
    slug = models.SlugField(db_index=True, unique=True)
    category = models.CharField(choices=EMOTION_CATEGORIES_CHOICES, max_length=30, default=JOY, db_index=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ('slug', )
        verbose_name = _("Emotion")
        verbose_name_plural = _("Emotions")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Emotion, self).save(*args, **kwargs)

    def __str__(self):
        return u"{} ({})".format(self.name, self.category)


@python_2_unicode_compatible
class Search(DateTimeModel):
    query = models.CharField(max_length=140)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    nlp_analysis = models.TextField(default='', help_text=_('json dump of Google NLP analysis'))

    class Meta:
        ordering = ('last_change_date', )
        verbose_name = _("Search")
        verbose_name_plural = _("Searches")

    def __str__(self):
        return u"{}".format(self.query)
