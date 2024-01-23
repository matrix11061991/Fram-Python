# my_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm, UserProfileForm

def home(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'home.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                # Redirigez l'utilisateur vers la page d'édition de profil après la connexion réussie
                return redirect('profile_edit')
            else:
                # Gestion des erreurs si l'authentification échoue
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid email or password.'})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_edit')  # Redirection vers la même page après la mise à jour
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'profile_edit.html', {'form': form})