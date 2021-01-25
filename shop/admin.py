from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.html import format_html
from .models import Shop

# Register your models here.

class ShopAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.product_photo.url))

    thumbnail.short_description = 'Product Photo'

    list_display = ('id', 'thumbnail', 'brand', 'categories', 'color', 'price')
    list_display_links = ('id', 'thumbnail')
    search_fields = ('brand', 'categories', 'color')
    list_filter = ('brand','categories')

admin.site.register(Shop, ShopAdmin)
