```bash
 ____ __     __   ___ _  _           __  __ ____ _  _ ____ ____ ____ _____  ____ ____ ____   
( ___|  )   /__\ / __| )/ )   ___   (  \/  |_  _| \( |_  _|  _ (  _ (  _  )(_  _| ___|_  _)  
 )__) )(__ /(__)\\__ \)  (   (___)   )    ( _)(_ )  ( _)(_ )___/)   /)(_)(.-_)(  )__)  )(    
(__) (____|__)(__|___(_)\_)         (_/\/\_|____|_)\_|____|__) (_)\_|_____)____)(____)(__)
```
## Etape 1 - Installer Flask : 
Si vous n'avez pas encore installé Flask, vous pouvez le faire en utilisant pip :
```bash
pip install flask
```

## Etape 2 - Créer la structure du projet : 
Organisez votre projet avec une structure de fichiers basique. Par exemple :
```bash
my_flask_project/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── img/
│       └── logo.png
├── templates/
│   ├── index.html
│   └── about.html
└── app.py
```

## Etape 3 - Écrire le code de l'application : 
Créez votre fichier **app.py** avec le code suivant :
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    message = "Bienvenue sur la page d'accueil"
    return render_template('index.html', message=message)

@app.route('/about')
def about():
    company_name = "Mon Entreprise"
    return render_template('about.html', company_name=company_name)

if __name__ == '__main__':
    app.run(debug=True)
```
Dans ce code, une route principale ('/') est définie pour renvoyer un modèle appelé 'index'. Une autre route ('/static/') est définie pour servir des fichiers statiques tels que des fichiers CSS et JS depuis le répertoire 'static'.

## Etape 4 - Écrire le modèle : 
Créez un fichier templates /index.html avec le contenu suivant :
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <title>Mon Projet Flask</title>
</head>
<body>
    <h1>{{ message }}</h1>
    <img src="{{ url_for('static', filename='img/logo.jpg') }}" alt="Logo">
    <a href="{{ url_for('about') }}">À propos de nous</a>
    <script src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>
```
Créez un fichier templates /about.html avec le contenu suivant :
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <title>À Propos de Nous</title>
</head>
<body>
    <h1>À Propos de Nous</h1>
    <p>Nous sommes {{ company_name }}</p>
    <img src="{{ url_for('static', filename='img/logo.jpeg') }}" alt="Logo">
    <script src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>
```
## Etape 5 - Ajouter des fichiers CSS et JS : 
Ajoutez vos fichiers CSS (style.css), JS (script.js) et images dans les répertoires respectifs sous le dossier static.
**static/css/style.css :**
```css
body {
    font-family: Arial, sans-serif;
    margin: 20px;
}

.header {
    text-align: center;
}

img {
    max-width: 100%;
    height: auto;
}
```
**static/js/script.js:**
```javascript
console.log('Script loaded.');
```
## Etape 6 - Exécuter l'application : 
Lancez votre application en exécutant le fichier app.py :
```bash
python app.py
```
Visitez http://127.0.0.1:5000/ dans votre navigateur pour voir votre application.

C'est tout ! Vous avez maintenant une application web simple avec le framework flask, intégrant des fichiers CSS et JS. Vous pouvez bien sûr étendre votre application en ajoutant plus de fonctionnalités et en améliorant le design.








