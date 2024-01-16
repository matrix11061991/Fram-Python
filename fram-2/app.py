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
