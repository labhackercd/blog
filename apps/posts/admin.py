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
    list_display = ['title', 'user', 'published_at']
    list_filter = ['status', 'published_at']
    search_fields = ['title', 'content', 'user']

admin.site.register(Post, PostAdmin)
