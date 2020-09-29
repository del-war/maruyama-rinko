from django.contrib import admin
from stockmgmt_2.models import Category_2, Stock_2
from stockmgmt_2.forms import StockCreateForm_2

# Register your models here.

class StockCreateAdmin_2(admin.ModelAdmin):
    list_display = ['category', 'item_name', 'quantity']
    form = StockCreateForm_2
    list_filter = ['category']
    search_fields = ['category', 'item_name']

admin.site.register(Stock_2, StockCreateAdmin_2)
admin.site.register(Category_2)
