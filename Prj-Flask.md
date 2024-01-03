# Fiche d'Activité Pratique :  Création d'un Petit Projet avec Flask Framework
## Objectif
L'objectif de cette activité pratique est de créer un projet Web simple en utilisant le framework Flask en Python. À la fin de cette activité, les participants auront mis en place un serveur Web basique avec quelques routes.

## Prérequis
* Python installé sur la machine
* Connaissance de base en programmation Python
## Étapes
**Étape 1: Installation de Flask**  
Assurez-vous que Flask est installé en exécutant la commande suivante dans votre terminal ou invite de commande :
```bash
pip install Flask
```
**Étape 2: Structure du Projet**  
Créez un dossier pour votre projet. À l'intérieur, créez le fichier principal **app.py**.

**Étape 3: Configuration de l'Application**  
Ouvrez le fichier app.py et ajoutez le code suivant pour configurer une application Web simple avec **Flask** :
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Bienvenue sur la page d'accueil!"

if __name__ == '__main__':
    app.run(debug=True)
```
**Étape 4:  Ajout de Pages Dynamiques**  
Créez un dossier templates/ pour stocker les fichiers HTML. À l'intérieur, créez un fichier **index.html** :
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
Modifiez ensuite le fichier app.py pour utiliser ce modèle :
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```
**Étape 5: Exécution de l'Application**  
Exécutez l'application en lançant le script **app.py**. Ouvrez votre navigateur et accédez à http://localhost:8080 pour voir le résultat.

## Conclusion
Félicitations ! Vous avez créé un petit projet Web avec le framework Flask en Python. Explorez davantage Flask pour ajouter des fonctionnalités supplémentaires à votre application.



