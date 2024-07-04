from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistroForm(UserCreationForm):
    pass

class LoginForm(AuthenticationForm):
    pass
