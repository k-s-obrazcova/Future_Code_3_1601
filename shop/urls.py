from django.urls import path
from .views import *
urlpatterns = [
    path('product/all/', product_list, name='product_list'),
    path('product/one-filter/', get_one_filter_product, name='get_one_filter'),
    path('product/more-filter/', get_more_filter_product, name='get_more_filter'),
    path('product/all-filter/', product_catalog_with_filter, name='product_list_filter'),
    path('product/detail/<int:id>/', get_one_product, name='get_one_product'),

    path('supplier/', ListSupplier.as_view(), name='supplier_list'),
    path('supplier/create/', CreateSupplier.as_view(), name='supplier_create'),
    path('supplier/detail/<int:pk>/', DetailSupplier.as_view(), name='supplier_detail'),
    path('supplier/update/<int:pk>/', UpdateSupplier.as_view(), name='supplier_update'),
    path('supplier/delete/<int:pk>/', DeleteSupplier.as_view(), name='supplier_delete'),
    
]