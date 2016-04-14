from django.contrib import admin

from ckeditor.widgets import CKEditorWidget
from django import forms
from image_cropping import ImageCroppingMixin

from apps.posts.models import Post


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        exclude = ('slug',)


class PostAdmin(ImageCroppingMixin, admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Post, PostAdmin)
