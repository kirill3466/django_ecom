from django.urls import path

from product.views import ProductView

from .views import ProductView

urlpatterns = [
    path('shop/<slug:slug>/', ProductView.as_view(), name='product'),
]
