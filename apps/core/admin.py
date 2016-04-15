from django.contrib import admin
from image_cropping import ImageCroppingMixin
from models import User


class UserAdmin(ImageCroppingMixin, admin.ModelAdmin):
    search_fields = ['username', 'first_name', 'last_name', 'email']
    list_filter = ['created_date']


admin.site.register(User, UserAdmin)
