from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class MyAccountView(View):
    def get(self, request):
        return render(request, 'account/my_account.html')


@method_decorator(login_required, name='dispatch')
class EditMyAccountView(View):
    def post(self, request):
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.save()
        return redirect('my_account')

    def get(self, request):
        return render(request, 'account/edit_account.html')
