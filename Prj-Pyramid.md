# Fiche d'Activité Pratique :  Création d'un Petit Projet avec Pyramid Framework
## Objectif
L'objectif de cette activité pratique est de créer un projet Web simple en utilisant le framework Pyramid en Python. À la fin de cette activité, les participants auront mis en place un serveur Web avec quelques vues.

## Prérequis
* Python installé sur la machine
* Connaissance de base en programmation Python
## Étapes
**Étape 1: Installation de Pyramid**  
Assurez-vous que Pyramid est installé en exécutant la commande suivante dans votre terminal ou invite de commande :
```bash
pip install "pyramid==2.0"
```
**Étape 2: Création du Projet**  
Ouvrez le terminal et créez un dossier pour votre projet. À l'intérieur de ce dossier, exécutez la commande suivante pour créer un nouveau projet Pyramid :
```bash
cookiecutter gh:Pylons/pyramid-cookiecutter-starter
```
Suivez les instructions pour configurer votre projet.
**Étape 3: Configuration de l'Application**  
Accédez au répertoire du projet et installez les dépendances :
```bash
cd nom_du_projet
pip install -e .
```
**Étape 4: Création d'une Vue**  
Ouvrez le fichier **views.py** dans le répertoire **nom_du_projet** et ajoutez une vue simple :
```python
from pyramid.view import view_config

@view_config(route_name='home', renderer='templates/home.jinja2')
def home(request):
    return {'content': 'Bienvenue sur la page d\'accueil!'}
```

**Étape 5: Configuration des Routes**  
Exécutez l'application en lançant le script **app.py**. Ouvrez votre navigateur et accédez à http://localhost:8080 pour voir le résultat.
from pyramid.config import Configurator
```python
def includeme(config):
    config.add_route('home', '/')
    config.scan('.views')

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('.routes')
    config.include('pyramid_jinja2')
    config.scan()
    return config.make_wsgi_app()
```
**Étape 6: Création d'un Template**  
Créez un dossier templates dans le répertoire nom_du_projet. À l'intérieur, créez un fichier home.jinja2 :
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
    <h1>{{ content }}</h1>
</body>
</html>
```
**Étape 7: Exécution du Serveur**  
Dans le terminal, exécutez le serveur Pyramid :
```bash
pserve development.ini
```
Ouvrez votre navigateur et accédez à http://localhost:6543 pour voir le résultat.
## Conclusion
Félicitations ! Vous avez créé un petit projet avec le framework Pyramid en Python. Explorez davantage Pyramid pour ajouter des fonctionnalités supplémentaires à votre application.
