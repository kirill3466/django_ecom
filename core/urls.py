from django.urls import path


from .views import FrontPageView, ShopView

urlpatterns = [
    path('', FrontPageView.as_view(), name='frontpage'),
    path('shop/', ShopView.as_view(), name='shop'),
]
