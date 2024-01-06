## Etape 1 - Installer Bottle : 
Si vous n'avez pas encore installé Bottle, vous pouvez le faire en utilisant pip :
```bash
pip install bottle
```

## Etape 2 - Créer la structure du projet : 
Organisez votre projet avec une structure de fichiers basique. Par exemple :
```bash
/le_nom_de_votre_application
├── app.py
├── static
│   ├── css
│   │   └── style.css
│   └── js
│       └── script.js
└── views
    └── index.tpl
```

## Etape 3 - Écrire le code de l'application : 
Créez votre fichier app.py avec le code suivant :
```python
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
```
Dans ce code, une route principale ('/') est définie pour renvoyer un modèle appelé 'index'. Une autre route ('/static/') est définie pour servir des fichiers statiques tels que des fichiers CSS et JS depuis le répertoire 'static'.

## Etape 4 - Écrire le modèle : 
Créez un fichier views/index.tpl avec le contenu suivant :
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ma Application</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <h1>Bienvenue sur ma page!</h1>
    <script src="/static/js/script.js"></script>
</body>
</html>
```
## Etape 5 - Ajouter des fichiers CSS et JS : 
Ajoutez vos fichiers CSS (style.css) et JS (script.js) dans les répertoires respectifs sous le dossier static.
**static/css/style.css :**
```css
body {
    background-color: #f0f0f0;
    font-family: Arial, sans-serif;
}

h1 {
    color: #333;
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
Votre application sera accessible à l'adresse http://localhost:8080/. Vous devriez voir le message "Bienvenue sur ma page!" avec le style CSS appliqué et le script JavaScript exécuté.

C'est tout ! Vous avez maintenant une application web simple avec le framework Bottle, intégrant des fichiers CSS et JS. Vous pouvez bien sûr étendre votre application en ajoutant plus de fonctionnalités et en améliorant le design.







