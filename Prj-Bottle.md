# Fiche d'Activité Pratique : Création d'un Petit Projet avec Bottle Framework
## Objectif
L'objectif de cette activité pratique est de créer un projet Web simple en utilisant le framework Bottle en Python. À la fin de cette activité, les participants auront mis en place un serveur Web basique avec quelques routes.
## Prérequis
* Python installé sur la machine
* Connaissance de base en programmation Python
## Étapes
**Étape 1: Installation de Bottle**
Assurez-vous que Bottle est installé en exécutant la commande suivante dans votre terminal ou invite de commande :
```sh
pip install bottle
```
**Étape 2: Structure du Projet**
Créez un dossier pour votre projet. À l'intérieur, créez le fichier principal app.py.

**Étape 3: Configuration de l'Application**
Ouvrez le fichier app.py et ajoutez le code suivant pour configurer une application Web simple avec **Bottle** :
```python
from bottle import route, run, template

@route('/')
def index():
    return "Bienvenue sur la page d'accueil!"

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
```
**Étape 4:  Ajout de Pages Dynamiques**
Modifiez la méthode index dans app.py pour renvoyer une page HTML dynamique :
```python
from bottle import route, run, template

@route('/')
def index():
    return template('index', title='Page d\'Accueil', content='Bienvenue sur la page d\'accueil!')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
```
**Étape 5: Création du Fichier HTML**
Créez un dossier views/ pour stocker les fichiers HTML. À l'intérieur, créez un fichier **index.tpl** :
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}}</title>
</head>
<body>
    <h1>{{content}}</h1>
</body>
</html>
```
**Étape 6: Exécution de l'Application**
Exécutez l'application en lançant le script **app.py**. Ouvrez votre navigateur et accédez à http://localhost:8080 pour voir le résultat.

## Conclusion
Félicitations ! Vous avez créé un petit projet Web avec le framework Bottle en Python. Explorez davantage Bottle pour ajouter des fonctionnalités supplémentaires à votre application.

## License
MatrixTera


