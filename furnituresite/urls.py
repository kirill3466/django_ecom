from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('core.urls')),
    path('', include('auth_app.urls')),
    path('', include('account.urls')),
    path('api/', include('api.urls')),
    path('orders/', include('orders.urls')),
    path('cart/', include('cart.urls')),
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('api-auth/', include('rest_framework.urls')),
] + debug_toolbar_urls()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
