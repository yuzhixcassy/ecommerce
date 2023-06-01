from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
from .models import *

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))

class CustomerRegistForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control', 'placeholder' : 'asdf'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder' : 'asdf'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder' : 'asdf'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder' : 'asdf'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ResetPasswordForm(PasswordChangeForm):
    pass

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['nama', 'daerah', 'kota', 'notelp', 'negara', 'kodepos']
        widget = {
            'nama' : forms.TextInput(attrs={'class':'form-control'}),
            'daerah' : forms.TextInput(attrs={'class':'form-control'}),
            'kota' : forms.TextInput(attrs={'class':'form-control'}),
            'notelp' : forms.NumberInput(attrs={'class':'form-control'}),
            'negara' : forms.Select(attrs={'class':'form-control'}),
            'kodepos' : forms.NumberInput(attrs={'class':'form-control'}),
        }

# class CustomerRegistForm(UserCreationForm):
#     fields = ['username', 'email', 'password1', 'password2']

#     labels = {
#         'password1': 'Password',
#         'password2': 'Confirm Password',
#     }

#     widgets = {
#         'username': forms.CharField(),
#         'email': forms.EmailField(),
#         'password1': forms.PasswordInput(),
#         'password2': forms.PasswordInput(),
#     }