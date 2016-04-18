from django.contrib import admin
from django import forms
from image_cropping import ImageCroppingMixin
from apps.posts.models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
            'content': CKEditorUploadingWidget(),
        }
        exclude = ('slug',)


class PostAdmin(ImageCroppingMixin, admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Post, PostAdmin)
