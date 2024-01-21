from django.shortcuts import render


def signup(request):
    return render(request, 'auth/signup.html')

def login(request):
    return render(request, 'auth/login.html')
