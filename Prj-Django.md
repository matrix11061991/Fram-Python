# Fiche d'Activité Pratique : Création d'un Petit Projet avec Django Framework
## Objectif
L'objectif de cette activité pratique est de créer un projet Web simple en utilisant le framework Django en Python. À la fin de cette activité, les participants auront mis en place un serveur Web avec une page d'accueil et une base de données simple.

## Prérequis
* Python installé sur la machine
* Connaissance de base en programmation Python
## Étapes
**Étape 1: Installation de Django**  
Assurez-vous que Django est installé en exécutant la commande suivante dans votre terminal ou invite de commande :
```bash
pip install Django
```
**Étape 2: Création du Projet**  
Créez un dossier pour votre projet. À l'intérieur, ouvrez le terminal et exécutez la commande suivante pour créer un nouveau projet Django :
```bash
django-admin startproject monprojet
```
**Étape 3: Configuration de l'Application**  
Entrez dans le répertoire du projet :
```bash
cd monprojet
```
Ouvrez le fichier **views.py** dans le répertoire **monprojet** et modifiez-le comme suit :
```python
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenue sur la page d'accueil!")
```
**Étape 4:  Configuration des URLs**  
Ouvrez le fichier **urls.py** dans le répertoire monprojet et configurez les URLs :
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
**Étape 5: Configuration de la Base de Données**  
Ouvrez le fichier settings.py dans le répertoire monprojet. Dans la section DATABASES, configurez la base de données SQLite :
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
```

**Étape 6: Exécution de Migrations**    
Dans le terminal, exécutez les migrations pour créer la base de données :
```bash
python manage.py migrate
```
**Étape 7: Création d'une Application**   
Créez une nouvelle application dans le projet :
```bash
python manage.py startapp monapp
```
**Étape 8: Ajout d'une Page Dynamique**    
Modifiez le fichier **views.py** dans le répertoire **monapp** :
```python
from django.shortcuts import render

def index(request):
    return render(request, 'monapp/index.html', {})
```

Créez un dossier templates dans le répertoire **monapp** et à l'intérieur, créez un fichier **index.html** :
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page d'Accueil</title>
</head>
<body>
    <h1>Bienvenue sur la page d'accueil!</h1>
</body>
</html>
```

**Étape 9: Configuration des URLs de l'Application**    
Modifiez le fichier urls.py dans le répertoire **monapp** :
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

**Étape 10: Configuration des URLs Principales**    
Modifiez le fichier **urls.py** dans le répertoire monprojet :
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('monapp.urls')),
]
```
**Étape 11: Exécution du Serveur**    
Dans le terminal, exécutez le serveur Django :
```bash
python manage.py runserver
```
Ouvrez votre navigateur et accédez à http://localhost:8000 pour voir le résultat.
## Conclusion
Félicitations ! Vous avez créé un petit projet avec le framework Django en Python. Explorez davantage Django pour ajouter des fonctionnalités supplémentaires à votre application.
