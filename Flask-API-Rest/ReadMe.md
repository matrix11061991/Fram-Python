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
