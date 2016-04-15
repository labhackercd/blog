# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import os
import random
import string
from django.utils.text import slugify
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from easy_thumbnails.files import get_thumbnailer
from image_cropping import ImageRatioField


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password=password)
        user.is_superuser = True
        user.save(using=self._db)
        return user


def update_filename(instance, filename):
    path = "uploads/user/"
    fname = filename.split('.')
    format = slugify(fname[0]) + ''.join([random.SystemRandom().choice(''.join(string.digits)) for i in range(8)]) + '.' + fname[-1]
    return os.path.join(path, format)


class User(AbstractBaseUser):
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    first_name = models.CharField('Primeiro nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=50, blank=True, null=True)
    email = models.EmailField(verbose_name='Email', max_length=255)
    username = models.CharField('username', max_length=50, unique=True)
    is_active = models.BooleanField('Ativo?', default=True)
    is_member = models.BooleanField('Membro?', default=True)
    is_superuser = models.BooleanField('Administrador?', default=False)
    created_date = models.DateTimeField('Criado em', default=datetime.now)
    photo = models.ImageField('Foto', upload_to=update_filename, blank=True, null=True)
    photo_thumb = ImageRatioField('photo', '110x110')
    description = models.TextField('Descrição', null=True, blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'

    def get_photo_thumb(self):
        return get_thumbnailer(self.photo).get_thumbnail({
            'size': (110, 110),
            'box': self.photo_thumb,
            'crop': True,
            'detail': True,
            }).url

    def __unicode__(self):
        return self.get_display_name()

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name]).strip()

    def get_short_name(self):
        return self.first_name

    def get_display_name(self):
        if self.first_name and self.last_name:
            return self.get_full_name()
        elif self.first_name and not self.last_name:
            return self.get_short_name()
        else:
            return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_superuser