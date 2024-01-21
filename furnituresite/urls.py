from django.contrib import admin
from django.urls import path

from cart.views import add_to_cart
from core.views import frontpage

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('admin/', admin.site.urls),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
]
