```bash
___________.__                 __    
\_   _____/|  | _____    _____|  | __
 |    __)  |  | \__  \  /  ___/  |/ /
 |     \   |  |__/ __ \_\___ \|    < 
 \___  /   |____(____  /____  >__|_ \
     \/              \/     \/     \/
```
## Etape 1 - Installer Flask : 
Si vous n'avez pas encore installé Flask, vous pouvez le faire en utilisant **pip** :
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
│   │   └── main.js
│   ├── img/
│   │   ├── avatars/
│   │   └── logo.png
│   └── scss/
│       └── (vos fichiers SCSS)
│   └── vendor/
│       └── (vos fichiers de fournisseurs externes, si nécessaire)
├── templates/
│   ├── base.html
│   ├── base-core.html
│   ├── components/
│   │   ├── header.html
│   │   ├── login_form.html
│   │   ├── logo.html
│   │   ├── registration_form.html
│   │   └── sidebar.html
│   ├── home.html
│   ├── index.html
│   ├── login.html
│   ├── profile.html
│   └── about.html
├── app.py
└── requirements.txt

```

## Etape 3 - Écrire le code de l'application : 
Créez votre fichier **app.py** avec le code suivant :
```python
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from flask_bcrypt import Bcrypt
import os
import mysql.connector

app = Flask(__name__)
app.secret_key = '11061991'
bcrypt = Bcrypt(app)
# Configuration du dossier avatars
app.config['DOSSIER_AVATARS'] = 'static/img/avatars'
# Configuration de la base de données
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="espaceM"
)
cursor = db.cursor()

# Page d'accueil
@app.route('/')
def index():
    msg = 'jrs'
    return render_template('index.html',msg=msg)

# Page d'inscription
@app.route('/inscription', methods=['POST'])
def inscription():
    nom = request.form['nom']
    prenom = request.form['prenom']
    email = request.form['email']
    mot_de_passe = request.form['mot_de_passe']

    # Hasher le mot de passe sans spécifier le sel
    mot_de_passe_hashe = bcrypt.generate_password_hash(mot_de_passe).decode('utf-8')

    # Insérer les données dans la base de données
    cursor.execute("INSERT INTO utilisateurs (nom,prenom ,email, mot_de_passe) VALUES (%s, %s, %s, %s)", (nom, prenom, email, mot_de_passe_hashe))
    db.commit()

    return redirect(url_for('index'))

# Page de connexion
@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    if request.method == 'POST':
        email = request.form['email']
        mot_de_passe = request.form['mot_de_passe']

        cursor.execute("SELECT * FROM utilisateurs WHERE email = %s", (email,))
        utilisateur = cursor.fetchone()
        print(utilisateur[3])
        if utilisateur and bcrypt.check_password_hash(utilisateur[3], mot_de_passe):
            # Mot de passe correct, connectez l'utilisateur
            session['utilisateur_id'] = utilisateur[0]
            return redirect(url_for('home'))
        else:
            # Mot de passe incorrect
            return render_template('login.html', erreur="Adresse email ou mot de passe incorrect.")

    return render_template('login.html')

# Page home
@app.route('/home')
def home():
    # Vérifier si l'utilisateur est connecté en vérifiant la session
    if 'utilisateur_id' in session:
        utilisateur_id = session['utilisateur_id']

        # Récupérer les informations de l'utilisateur depuis la base de données
        cursor.execute("SELECT * FROM utilisateurs WHERE id = %s", (utilisateur_id,))
        utilisateur = cursor.fetchone()

        if utilisateur:
            print("Informations de l'utilisateur récupérées :", utilisateur)
            return render_template('home.html', utilisateur=utilisateur)
        else:
            print("Aucun utilisateur trouvé pour l'ID :", utilisateur_id)
            return render_template('home.html', utilisateur=None)
    else:
        # Rediriger vers la page de connexion si l'utilisateur n'est pas connecté
        return redirect(url_for('connexion'))

# Route pour la modification de profil
@app.route('/modifier_profil', methods=['POST'])
def modifier_profil():
    if 'utilisateur_id' in session:
        utilisateur_id = session['utilisateur_id']

        nouveau_nom = request.form['nom']
        nouveau_prenom = request.form['prenom']
        
        # Vérifier si un fichier a été téléchargé
        if 'avatar' in request.files:
            avatar = request.files['avatar']
            
            # Vérifier si un fichier a été sélectionné
            if avatar.filename != '':
                # Créer un sous-dossier pour l'utilisateur s'il n'existe pas déjà
                dossier_avatars_utilisateur = os.path.join(app.config['DOSSIER_AVATARS'], str(utilisateur_id))
                
                if not os.path.exists(dossier_avatars_utilisateur):
                    os.makedirs(dossier_avatars_utilisateur)

                nom_avatar = secure_filename(avatar.filename)
                chemin_sauvegarde = os.path.join(dossier_avatars_utilisateur, nom_avatar)
                avatar.save(chemin_sauvegarde)

                # Mettre à jour le champ avatar dans la base de données
                cursor.execute("UPDATE utilisateurs SET nom = %s, prenom = %s, avatar = %s WHERE id = %s",
                               (nouveau_nom, nouveau_prenom, nom_avatar, utilisateur_id))
            else:
                # Mettre à jour les informations de l'utilisateur dans la base de données sans changer l'avatar
                cursor.execute("UPDATE utilisateurs SET nom = %s, prenom = %s WHERE id = %s",
                               (nouveau_nom, nouveau_prenom, utilisateur_id))

            db.commit()

            return redirect(url_for('home'))
        else:
            # Rediriger vers la page de connexion si l'utilisateur n'est pas connecté
            return redirect(url_for('connexion'))

# Route pour la page d'edition du profil
@app.route('/profile')
def profile():
    # Vérifier si l'utilisateur est connecté en vérifiant la session
    if 'utilisateur_id' in session:
        utilisateur_id = session['utilisateur_id']

        # Récupérer les informations de l'utilisateur depuis la base de données
        cursor.execute("SELECT * FROM utilisateurs WHERE id = %s", (utilisateur_id,))
        utilisateur = cursor.fetchone()

        if utilisateur:
            print("Informations de l'utilisateur récupérées :", utilisateur)
            return render_template('profile.html', utilisateur=utilisateur)
        else:
            print("Aucun utilisateur trouvé pour l'ID :", utilisateur_id)
            return render_template('profile.html', utilisateur=None)
    else:
        # Rediriger vers la page de connexion si l'utilisateur n'est pas connecté
        return redirect(url_for('connexion'))

# Route pour la déconnexion
@app.route('/deconnexion')
def deconnexion():
    # Supprimer l'identifiant de l'utilisateur de la session
    session.pop('utilisateur_id', None)
    # Rediriger vers la page de connexion
    return redirect(url_for('connexion'))


if __name__ == '__main__':
    app.run(debug=True)

```
Dans ce code, une route principale **('/')** est définie pour renvoyer un modèle appelé 'index'. Une autre route **('/static/')** est définie pour servir des fichiers statiques tels que des fichiers CSS et JS depuis le répertoire 'static'.

## Etape 4 - Écrire le modèle : 
Créez un fichier **templates /index.html** avec le contenu suivant :
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
Créez un fichier **templates /about.html** avec le contenu suivant :
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
Lancez votre application en exécutant le fichier **app.py** :
```bash
python app.py
```
Visitez http://127.0.0.1:5000/ dans votre navigateur pour voir votre application.

C'est tout ! Vous avez maintenant une application web simple avec le framework flask, intégrant des fichiers CSS et JS. Vous pouvez bien sûr étendre votre application en ajoutant plus de fonctionnalités et en améliorant le design.








