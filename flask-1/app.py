# Importation des modules nécessaires
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, SubmitField

# Initialisation de l'application Flask
app = Flask(__name__)

# Configuration de la base de données SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Définition du modèle de données (table User)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)

# Définition du formulaire d'inscription avec WTForms
class RegistrationForm(Form):
    username = StringField('Nom d\'utilisateur', render_kw={'placeholder': 'Entrez votre nom d\'utilisateur'})
    submit = SubmitField('S\'inscrire')

# Route principale - Page d'accueil
@app.route('/')
def index():
    # Récupération de tous les utilisateurs de la base de données
    users = User.query.all()
    
    # Création d'une instance du formulaire d'inscription
    form = RegistrationForm(request.form)
    
    # Message de bienvenue
    message = "Bienvenue sur la page d'accueil"
    
    # Rendu du template index.html en passant les utilisateurs, le formulaire et le message
    return render_template('index.html', users=users, form=form, message=message)

# Route pour le traitement de l'inscription (reçoit les données du formulaire)
@app.route('/register', methods=['POST'])
def register():
    # Création d'une instance du formulaire d'inscription avec les données reçues
    form = RegistrationForm(request.form)
    
    # Vérification de la validité du formulaire
    if form.validate():
        # Création d'un nouvel utilisateur avec le nom d'utilisateur du formulaire
        new_user = User(username=form.username.data)
        
        # Ajout de l'utilisateur à la session de base de données
        db.session.add(new_user)
        
        # Commit des changements dans la base de données
        db.session.commit()
        
        # Redirection vers la page d'accueil
        return redirect(url_for('index'))
    
    # Rendu du template index.html avec le formulaire en cas d'erreur de validation
    return render_template('index.html', form=form)

# Route pour la page "À Propos"
@app.route('/about')
def about():
    # Définition d'une variable pour le nom de l'entreprise
    company_name = "Mon Entreprise"
    
    # Rendu du template about.html en passant le nom de l'entreprise
    return render_template('about.html', company_name=company_name)

# Exécution de l'application Flask
if __name__ == '__main__':
    # Création de toutes les tables de la base de données (si elles n'existent pas)
    with app.app_context():
        db.create_all()
    
    # Démarrage de l'application en mode débogage
    app.run(debug=True)