from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegisterForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

# class UserLoginForm(AuthenticationForm):
    
#     class Meta(AuthenticationForm.Meta):
#         model = User
#         fields = ['username', 'password']