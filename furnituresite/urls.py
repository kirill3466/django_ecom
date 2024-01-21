from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('core.urls')),
    path('cart/', include('cart.urls')),
    path('admin/', admin.site.urls),
    path('', include('auth_app.urls')),
]
