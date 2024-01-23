from django.urls import path

from account.views import edit_myaccount, my_account

urlpatterns = [
    path('my_account/', my_account, name='my_account'),
    path('edit_myaccount/', edit_myaccount, name='edit_myaccount'),
]
