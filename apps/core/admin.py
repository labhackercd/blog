# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.forms.widgets import PasswordInput
from image_cropping import ImageCroppingMixin
from models import User
from django.utils.translation import ugettext_lazy as _


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        widgets = {
            'password': PasswordInput(),
        }
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'is_member', 'is_superuser',
                  'created_date', 'photo', 'photo_thumb', 'description')

    def save(self, commit=True):
        user = super(UserAdminForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdmin(ImageCroppingMixin, admin.ModelAdmin):
    search_fields = ['username', 'first_name', 'last_name', 'email']
    list_filter = ['created_date']
    list_display = ['get_display_name', 'email', 'is_superuser']
    form = UserAdminForm
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Pessoal'), {'fields': ('first_name', 'last_name', 'photo', 'photo_thumb', 'description')}),
        (_('Acesso'), {'fields': ('is_active', 'is_member', 'is_superuser')}),
        (_('Datas'), {'fields': ('last_login', 'created_date')}),
    )

admin.site.register(User, UserAdmin)
