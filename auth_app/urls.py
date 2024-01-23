from django.contrib.auth.views import LoginView
from django.urls import path

from .views import signup, logoutUser

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('logout/', logoutUser, name="logout"),
    path('login/', LoginView.as_view(template_name='auth/login.html'),
         name='login'),
]
