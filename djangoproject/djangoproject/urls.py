from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chiba/', include('stockmgmt.urls')),
    path('ota/', include('stockmgmt_2.urls')),
    path('', views.home, name='home'),

]
