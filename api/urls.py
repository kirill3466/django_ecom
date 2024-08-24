from django.urls import path

from .views import ProductViewSet, test

urlpatterns = [
    path('products/', ProductViewSet.as_view({'get': 'list'})),
    path('test/', test),
]
