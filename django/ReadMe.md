
# Fiche d'Activité Pratique - Création d'un CRUD avec Django et MySQL

## Objectif de l'Activité

Le but de cette activité est de permettre aux apprenants de créer un simple CRUD (Create, Read, Update, Delete) en utilisant le framework Django avec une base de données MySQL.

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
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'rascof',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True,
            'use_pure': True,
            'charset': 'utf8mb4',
        },
    },
}
```
- Pour plus tard, ajoutez egalement la ligne:
```python
AUTH_USER_MODEL = 'my_app.UserProfile'
```
### 3. Définition du Modèle

- Modifiez le fichier **my_app/models.py** pour définir le modèle de l'utilisateur avec les champs spécifiés.

```python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```
### 4. Appliquer les Migrations

- Exécutez les commandes `python manage.py makemigrations` et `python manage.py migrate` pour créer les tables dans la base de données.

### 5. Configuration de la Base de Données MySQL

- Modifiez le fichier `settings.py` pour configurer la base de données MySQL dans la section `DATABASES`.

### 6. Création des Vues

- Dans le fichier `views.py` de l'application, créez des vues pour lister, afficher, créer, mettre à jour et supprimer des tâches.

### 7. Création des Templates

- Créez des fichiers HTML dans le dossier `templates` de l'application pour chaque vue.

### 8. Configuration des URL

- Dans le fichier `urls.py` de l'application, configurez les URL pour utiliser les vues créées.

### 9. Inclusion des URL dans le Projet

- Dans le fichier `urls.py` du projet, incluez les URL de l'application.

### 10. Exécution du Serveur

- Exécutez le serveur de développement Django en utilisant la commande `python manage.py runserver`.

### 11. Test de l'Application

- Accédez à l'application à l'adresse http://127.0.0.1:8000/ dans un navigateur.
- Testez les fonctionnalités CRUD en ajoutant, modifiant et supprimant des tâches.
## Questions de Réflexion

1. Quel est le rôle du modèle dans une application Django?
2. Comment les migrations sont-elles utilisées pour mettre à jour la base de données?
3. Quelle est la différence entre les vues génériques et les vues personnalisées dans Django?
4. Comment Django gère-t-il les URL dans une application?
