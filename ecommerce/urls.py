from django.contrib import admin
from django.urls import path
from catalog.views import product_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', product_list, name='product_list'),
]
