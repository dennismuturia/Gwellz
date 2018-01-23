from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout
)
from django.shortcuts import render
# Create your views here.

def login_view(request):
    return render(request, 'user.html', {})

def register_view(request):
    return render(request, 'user.html', {})

def logout_view(request):
    return render(request, 'user.html', {})