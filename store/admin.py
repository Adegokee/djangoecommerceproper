from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['product_name', 'stock', 'price', 'cartegory', 'created_date', 'modify_date']
    prepopulated_fields={'slug': ['product_name'],}
    fieldsets=[]
    list_display_links=['product_name', 'stock', 'price', 'cartegory', 'created_date', 'modify_date']
    list_filter=[]
    

admin.site.register(Product, ProductAdmin)