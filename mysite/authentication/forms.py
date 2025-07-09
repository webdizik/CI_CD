from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)