from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect


def login_user(request):
    username = 'root'
    password = '123'
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return redirect('index')

    return redirect('index')


def logout_user(request):
    logout(request)
    return redirect('index')

