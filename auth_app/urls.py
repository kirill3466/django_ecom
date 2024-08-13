from django.contrib.auth.views import LoginView
from django.urls import path

from .views import LogoutView, SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path(
        'login/', LoginView.as_view(template_name='auth/login.html'),
        name='login'
    ),
]
