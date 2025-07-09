from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import LoginForm, RegisterForm


# Define a view function for the home page
def home(request):
    return render(request, 'authentication/home.html')

# Define a view function for the registration page
def register_page(request):
    form = RegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()               # Сохраняем нового пользователя
            login(request, user)             # Выполняем вход
            return redirect('post_list')     # Перенаправляем на главную страницу
    else:
        form = RegisterForm()
    return render(request, 'authentication/register.html', {'form': form})

# Define a view function for the login page
def login_page(request):
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)    # Проверяем учетные данные
            if user is not None:
                login(request, user)                            # Выполняем вход
                return redirect('post_list')                    # Перенаправляем на главную страницу

    return render(request, 'authentication/login.html', {'form': form})
