## Etape 1 - Installer Bottle : 
Si vous n'avez pas encore installé Bottle, vous pouvez le faire en utilisant pip :
pip install bottle

## Etape 2 - Créer la structure du projet : 
Organisez votre projet avec une structure de fichiers basique. Par exemple :
/le_nom_de_votre_application
├── app.py
├── static
│   ├── css
│   │   └── style.css
│   └── js
│       └── script.js
└── views
    └── index.tpl

## Etape 3 - Écrire le code de l'application : 
Créez votre fichier app.py avec le code suivant :
from bottle import Bottle, run, template, static_file

app = Bottle()

@app.route('/')
def index():
    return template('index')

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)

Dans ce code, une route principale ('/') est définie pour renvoyer un modèle appelé 'index'. Une autre route ('/static/') est définie pour servir des fichiers statiques tels que des fichiers CSS et JS depuis le répertoire 'static'.

## Etape 4 - Écrire le modèle : 
Créez un fichier views/index.tpl avec le contenu suivant :
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ma Application</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <h1>Bienvenue sur ma application!</h1>
    <script src="/static/js/script.js"></script>
</body>
</html>




