from django.contrib import admin
from image_cropping import ImageCroppingMixin
from apps.posts.forms import PostAdminForm
from apps.posts.models import Post


class PostAdmin(ImageCroppingMixin, admin.ModelAdmin):
    form = PostAdminForm
    list_display = ['title', 'user', 'published_at']
    list_filter = ['status', 'published_at']
    search_fields = ['title', 'content', 'user']

admin.site.register(Post, PostAdmin)
