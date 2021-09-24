from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def index(request):
    context = {
        'title': 'User System App'
    }
    return render(request, 'loginSystem/index.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, message='Account has been created. You\'re now able to')
            return redirect(reverse('loginSystem:login'))
    else:
        form = UserRegisterForm()
    context = {
        'title': 'Registration Page',
        'form': form
    }
    return render(request, 'loginSystem/register.html', context)


# def login(request):
#     return render(request, 'loginSystem/login.html')
