from django.urls import path

from account.views import EditMyAccountView, MyAccountView

urlpatterns = [
    path('my_account/', MyAccountView.as_view(), name='my_account'),
    path('edit_myaccount/', EditMyAccountView.as_view(), name='edit_myaccount'),
]
