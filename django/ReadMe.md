
# Fiche d'Activité Pratique - Création d'une application simple avec Django et MySQL

## Objectif de l'Activité

Le but de cette activité est de permettre aux apprenants de créer une application simple en utilisant le framework Django avec une base de données MySQL.

## Prérequis

1. Connaissance de base de Python.
2. Installation préalable de Django et MySQL connector.

## Étapes de l'Activité

### 1. Création du Projet Django

- Créez un nouveau projet Django appelé **my_project** en utilisant la commande suivante dans votre terminal ou invite de commande :
```sh
django-admin startproject my_project
```
- Allez dans le répertoire du projet en utilisant la commande:

```sh
cd my_project
```

### 2. Création de l'Application Django

- Créez une nouvelle application Django appelée **my_app** :
```sh
python manage.py startapp my_app
```
- Ouvrez le fichier **my_project/settings.py** et ajoutez la configuration de la base de données:
```python
# my_project/settings.py

# Configuration de la base de données
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',  # Utilisation du moteur MySQL avec le connecteur Django
        'NAME': 'rascof',  # Nom de la base de données
        'USER': 'root',  # Nom d'utilisateur pour se connecter à la base de données
        'PASSWORD': '',  # Mot de passe pour se connecter à la base de données
        'HOST': 'localhost',  # Adresse du serveur de base de données (dans ce cas, localhost)
        'PORT': '3306',  # Port sur lequel le serveur de base de données écoute (dans ce cas, 3306 pour MySQL)
        'OPTIONS': {
            'autocommit': True,  # Activer l'autocommit pour chaque transaction
            'use_pure': True,  # Utiliser le mode "pur" pour éviter des dépendances supplémentaires
            'charset': 'utf8mb4',  # Jeu de caractères à utiliser pour la base de données (utf8mb4 pour le support Unicode complet)
        },
    },
}
```
- Pour plus tard, ajoutez egalement la ligne:
```python
# Spécification du modèle d'utilisateur personnalisé
AUTH_USER_MODEL = 'my_app.UserProfile'
```
### 3. Définition du Modèle

- Modifiez le fichier **my_app/models.py** pour définir le modèle de l'utilisateur avec les champs spécifiés.

```python
# models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Gestionnaire personnalisé pour le modèle d'utilisateur
class UserProfileManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        # Vérifier si l'adresse e-mail est fournie
        if not email:
            raise ValueError('The Email field must be set')
        
        # Normaliser l'adresse e-mail
        email = self.normalize_email(email)
        
        # Créer un nouvel utilisateur avec les champs spécifiés
        user = self.model(email=email, username=username, **extra_fields)
        
        # Définir le mot de passe pour l'utilisateur
        user.set_password(password)
        
        # Sauvegarder l'utilisateur dans la base de données
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        # Définir les champs supplémentaires pour un superutilisateur
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Appeler la méthode create_user pour créer un superutilisateur
        return self.create_user(email, username, password, **extra_fields)

# Modèle d'utilisateur personnalisé
class UserProfile(AbstractBaseUser, PermissionsMixin):
    # Champs du modèle d'utilisateur
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    telephone = models.CharField(max_length=15)
    ville = models.CharField(max_length=255)
    description = models.TextField()

    # Champs pour la gestion des autorisations et de l'activation du compte
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Utilisation du gestionnaire personnalisé
    objects = UserProfileManager()

    # Champ utilisé comme identifiant lors de l'authentification
    USERNAME_FIELD = 'email'
    
    # Champs supplémentaires requis lors de la création d'un utilisateur
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        # Méthode pour représenter l'objet sous forme de chaîne
        return self.username
```
- Enregistrez le modèle en ajoutant 'my_app' à la liste INSTALLED_APPS dans **my_project/settings.py**:
```sh
# my_project/settings.py
INSTALLED_APPS = [
    # ...
    'my_app',
]
```
### 4. Appliquer les Migrations

- Exécutez les commandes `python manage.py makemigrations` et `python manage.py migrate` pour créer les tables dans la base de données.

### 5. Formulaire
Créez un formulaire Django pour l'inscription dans **my_app/forms.py**:
```python
# my_app/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

# Formulaire d'inscription personnalisé basé sur UserCreationForm
class RegistrationForm(UserCreationForm):
    class Meta:
        model = UserProfile  # Utilisation du modèle UserProfile
        fields = ['username', 'email', 'password1', 'password2', 'address', 'job', 'telephone', 'ville', 'description']

# Formulaire de connexion simple
class LoginForm(forms.Form):
    email = forms.EmailField()  # Champ pour l'adresse e-mail
    password = forms.CharField(widget=forms.PasswordInput)  # Champ pour le mot de passe avec widget de mot de passe

# Formulaire de profil utilisateur basé sur le modèle UserProfile
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile  # Utilisation du modèle UserProfile
        fields = ['username', 'email', 'address', 'job', 'telephone', 'ville', 'description']

```

### 6. Création des Vues
Créez une vue pour la page d'accueil avec le formulaire dans my_app/views.py:
```python
# my_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm, UserProfileForm

# Vue pour la page d'accueil avec le formulaire d'inscription
def home(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirection vers la page d'accueil après l'inscription réussie
    else:
        form = RegistrationForm()

    return render(request, 'home.html', {'form': form})

# Vue pour la page de connexion avec le formulaire de connexion
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Authentification de l'utilisateur
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

# Vue pour la page de modification de profil (accessible uniquement aux utilisateurs connectés)
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
```
### 7. Création des Templates

- Créez des fichiers HTML dans le dossier **templates** de l'application pour chaque vue:
Pour **my_app/templates/home.html**:
```html
<!-- my_app/templates/home.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Project</title>
</head>
<body>
    <h1>Home</h1>
    <form method="post" action="{% url 'home' %}">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Register</button>
    </form>
    <!-- Ajoutez ce lien pour rediriger vers la page de connexion -->
    <a href="{% url 'user_login' %}">Login</a>
</body>
</html>
```
Pour **my_app/templates/login.html**:
```html
<!-- my_app/templates/login.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    
    {% if error_message %}
        <p style="color: red;">{{ error_message }}</p>
    {% endif %}
    
    <form method="post" action="{% url 'user_login' %}">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Login</button>
    </form>
    <a href="{% url 'home' %}">Login</a>
</body>
</html>

```
Pour **my_app/templates/profile_edit.html**:
```html
<!-- my_app/templates/profile_edit.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Profile</title>
</head>
<body>
    <h1>Edit Profile</h1>

    <form method="post" action="{% url 'profile_edit' %}">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save Changes</button>
    </form>
</body>
</html>
```
### 8. Configuration des URL
Configurez les URL pour votre application dans my_app/urls.py :
```python
# my_app/urls.py
# my_app/urls.py
from django.urls import path
from .views import home, user_login, profile_edit

urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='user_login'),
    path('profile/edit/', profile_edit, name='profile_edit'),
]

```
### 9. Inclusion des URL dans le Projet
- Dans le fichier **urls.py** du projet, incluez les URL de l'application.
```python
# my_project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls')),
]
```
### 10. Exécution du Serveur

- Exécutez le serveur de développement Django en utilisant la commande `python manage.py runserver`.

### 11. Test de l'Application

- Accédez à l'application à l'adresse http://127.0.0.1:8000/ dans un navigateur.
- Testez les fonctionnalités CRUD en ajoutant, modifiant et supprimant des tâches.

# Liste des commandes Django avec leurs descriptions
1. **django-admin startproject [nom_projet]**
   - Crée un nouveau projet Django avec le nom spécifié.

2. **python manage.py startapp [nom_application]**
   - Crée une nouvelle application Django avec le nom spécifié dans le projet.

3. **python manage.py runserver**
   - Lance le serveur de développement pour le projet.

4. **python manage.py migrate**
   - Applique toutes les migrations en attente pour mettre à jour la base de données.

5. **python manage.py makemigrations**
   - Génère de nouvelles migrations en fonction des modifications dans les modèles.

6. **python manage.py createsuperuser**
   - Crée un superutilisateur qui peut accéder à l'interface d'administration Django.

7. **python manage.py shell**
   - Ouvre une console interactive basée sur Python pour interagir avec le projet.

8. **python manage.py test [nom_application]**
   - Exécute les tests pour l'application spécifiée.

9. **python manage.py collectstatic**
   - Collecte tous les fichiers statiques dans un répertoire pour une utilisation en production.

10. **python manage.py shell_plus**
    - Ouvre une console interactive améliorée avec des fonctionnalités supplémentaires grâce au package django-extensions.

11. **python manage.py dbshell**
    - Ouvre une interface de ligne de commande pour la base de données en cours d'utilisation.

12. **python manage.py showmigrations**
    - Affiche la liste des migrations et indique celles qui ont déjà été appliquées.

13. **python manage.py flush**
    - Supprime toutes les données de la base de données sans affecter le schéma.

14. **python manage.py runserver [adresse_ip:port]**
    - Lance le serveur de développement sur une adresse IP et un port spécifiés.

15. **python manage.py check**
    - Vérifie la configuration du projet pour détecter d'éventuelles erreurs et problèmes.

16. **python manage.py dumpdata > fichier.json**
    - Exporte les données de la base de données dans un fichier JSON.

17. **python manage.py loaddata fichier.json**
    - Importe les données depuis un fichier JSON dans la base de données.

## Questions de Réflexion

1. Quel est le rôle du modèle dans une application Django?
2. Comment les migrations sont-elles utilisées pour mettre à jour la base de données?
3. Quelle est la différence entre les vues génériques et les vues personnalisées dans Django?
4. Comment Django gère-t-il les URL dans une application?
