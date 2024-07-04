from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1']))
            return redirect('landing')
    else:
        form = RegistroForm()
    return render(request, 'autenticacion/registro.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('landing')
    else:
        form = LoginForm()
    return render(request, 'autenticacion/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('landing')
