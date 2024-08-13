from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.views import View

from .forms import SignUpForm


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'auth/signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            form = SignUpForm()
        return render(request, 'auth/signup.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')
