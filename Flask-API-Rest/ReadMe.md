# Fiche de Travaux Pratiques : API REST d'Inscription d'Utilisateur avec Flask

## Objectif

L'objectif de cette séance est de créer une API REST avec Flask permettant l'inscription d'un utilisateur en base de données.

## Prérequis

- Python installé sur votre système.
- Flask installé (vous pouvez l'installer avec `pip install Flask`).
- SQLite ou une autre base de données installée et configurée.

## Étapes

### Étape 1: Initialisation du Projet

1. Créez un nouveau dossier pour le projet.
2. À l'intérieur de ce dossier, créez un fichier `app.py` pour le code de l'application.

### Étape 2: Installation des Packages

Installez les packages nécessaires pour la base de données et la gestion des mots de passe :

```bash
pip install Flask Flask-SQLAlchemy Flask-Bcrypt
```
### Étape 3: Configuration de l'Application
Dans app.py, configurez l'application Flask avec une base de données SQLite et le cryptage des mots de passe :
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Utilisation de SQLite
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
```
### Étape 4: Création du Modèle Utilisateur
Ajoutez la définition du modèle utilisateur dans app.py :
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
```
### Étape 5: Création de la Route d'Inscription
Ajoutez une route pour l'inscription des utilisateurs dans app.py :
```python
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()

        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

        new_user = User(username=data['username'], email=data['email'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully!'})

    return jsonify({'message': 'Welcome to the registration page!'})
```
### Étape 6: Exécution de l'Application
Exécutez l'application avec la commande suivante dans le terminal :
```bash
python app.py
```
Vous pouvez utiliser un outil comme Postman ou cURL pour envoyer des requêtes POST à l'URL http://127.0.0.1:5000/register avec les données JSON appropriées.

Lien utile: https://openclassrooms.com/fr/courses/4525361-realisez-un-dashboard-avec-tableau/5774811-creez-une-api-avec-flask

## Conclusion
Vous avez créé une API REST avec Flask qui permet l'inscription d'un utilisateur en base de données. N'oubliez pas de gérer les erreurs et d'ajouter des fonctionnalités telles que la validation des champs avant d'ajouter ces fonctionnalités à un projet en production.
