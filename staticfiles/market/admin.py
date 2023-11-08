from django.contrib import admin
from .models import Product,Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['category','name','price','is_sold','publish','seller']
    prepopulated_fields={'slug':('name',)}
    raw_id_fields=['seller']
    list_filter=['publish','created_at','updated_at']
    
