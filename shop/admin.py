from django.contrib import admin
from .models import *

class ItemImageAdmin(admin.TabularInline):
    model = ItemImage
    extra = 1


class ColorItemQuantityAdmin(admin.TabularInline):
    model = ColorItemQuantity
    extra = 1


class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageAdmin, ColorItemQuantityAdmin]

admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(Color)

