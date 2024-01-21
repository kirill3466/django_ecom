from django.urls import path

from cart.views import add_to_cart
from product.views import product

from .views import frontpage, shop

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart')
]
