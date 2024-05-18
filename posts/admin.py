from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",),}
    list_display = ('name', 'id')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'adres', 'city', 'phone', 'email')
    search_fields = ('name', 'adres', 'city', 'phone', 'email')

@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'supplier', 'price', 'actual_quantity')
    list_filter = ('category', 'supplier')
    search_fields = ['title', 'name', 'supplier']
