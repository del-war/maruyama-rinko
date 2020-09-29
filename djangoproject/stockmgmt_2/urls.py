from django.urls import path
from stockmgmt_2 import views

app_name = 'stockmgmt_2'

urlpatterns = [
    path('list_product/', views.list_product, name='list_product'),
    path('add_item/',views.add_product, name='add_product'),
    path('update_product/<str:pk>/',views.update_product, name='update_product'),
    path('delete_product/<str:pk>/',views.delete_product, name='delete_product'),
    path('export_product/<str:pk>/',views.export_product, name='export_product'),
    path('import_product/<str:pk>/',views.import_product, name='import_product'),
    path('stock_details_product/<str:pk>/',views.stock_details_product, name='stock_details_product'),
    path('reorder_product_level/<str:pk>/',views.reorder_product_level, name='reorder_product_level'),
    path('list_product_history/',views.list_product_history, name='list_product_history'),


]
