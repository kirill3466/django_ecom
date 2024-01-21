from django.urls import path

from product.views import product

from .views import frontpage, shop

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
]
