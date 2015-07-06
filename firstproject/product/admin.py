from product.models import *
from django.contrib import admin

class Product_detailAdmin(admin.ModelAdmin):

    fields=['product_name','price','product_model']
    list_display = ('product_name','price','product_model')
    list_filter = ['price']
    search_fields = ['product_name']
    list_per_page = 50
    
admin.site.register(Product_detail,Product_detailAdmin)
