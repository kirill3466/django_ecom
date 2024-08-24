from django.urls import path

from cart.views import (
                        CartMenuView,
                        CartSuccessView,
                        CartTotalView,
                        add_to_cart,
                        cart,
                        checkout,
                        update_cart,
)

urlpatterns = [
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update_cart/<int:product_id>/<str:action>/',
         update_cart, name='update_cart'),
    path('hx_menu_cart/', CartMenuView.as_view(), name='hx_menu_cart'),
    path('hx_cart_total/', CartTotalView.as_view(), name='hx_cart_total'),
    path('success/', CartSuccessView.as_view(), name='success'),
]
