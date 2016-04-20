from __future__ import unicode_literals

from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    class_icon = models.CharField(max_length=50, null=True, blank=True)
    link = models.URLField()

    class Meta:
        verbose_name = 'Item de menu'
        verbose_name_plural = 'Itens do menu'
        ordering = ['id']

    def __unicode__(self):
        return self.name
