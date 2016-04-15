# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify

from image_cropping import ImageRatioField
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from datetime import datetime
from apps.core.models import User


class Post(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    title = models.CharField('Título', max_length=100)
    content = RichTextField('Conteúdo')
    image = models.ImageField('Foto', upload_to='uploads/post/images', null=True, blank=True)
    featured_image = ImageRatioField('image', '700x227', verbose_name='Imagem em Destaque')
    slug = models.SlugField(max_length=150, blank=True)
    tags = TaggableManager()
    status = models.BooleanField(default=True)
    published_at = models.DateTimeField(verbose_name='Data de Publicacao', default=datetime.now)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-published_at']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'year': self.published_at.year,
                                              'month': self.published_at.month,
                                              'day': self.published_at.day,
                                              'slug': self.slug})


def post_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

signals.pre_save.connect(post_pre_save, sender=Post)
