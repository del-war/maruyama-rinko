from django.urls import path
from stockmgmt import views

app_name = 'stockmgmt'

urlpatterns=[
    path('login_page/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('list_product/', views.list_product, name='list_product'),
    path('add_product/', views.add_product, name='add_product'),
    path('update_product/<str:pk>/', views.update_product, name='update_product'),
    path('delete_product/<str:pk>/', views.delete_product, name='delete_product'),
    path('stock_detail/<str:pk>/', views.stock_detail, name='stock_detail'),
    path('export_product/<str:pk>/', views.export_product, name='export_product'),
    path('import_product/<str:pk>/', views.import_product, name='import_product'),
    path('reorder_level/<str:pk>/', views.reorder_level, name='reorder_level'),
    path('list_product_history', views.list_product_history, name='list_product_history'),
]
