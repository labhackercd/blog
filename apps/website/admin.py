from django.contrib import admin
from models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'link']
    search_fields = ['name']

admin.site.register(MenuItem, MenuItemAdmin)
