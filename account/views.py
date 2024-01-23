from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


@login_required
def my_account(request):
    return render(request, 'account/my_account.html')


@login_required
def edit_myaccount(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.save()

        return redirect('my_account')
    return render(request, 'account/edit_account.html')
