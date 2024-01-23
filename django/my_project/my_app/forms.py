# my_app/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class RegistrationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password1', 'password2', 'address', 'job', 'telephone', 'ville', 'description']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'address', 'job', 'telephone', 'ville', 'description']