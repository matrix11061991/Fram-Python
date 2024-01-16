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
 - Dans `base-core.html`, créez une mise en page de base avec les éléments communs à toutes les pages (en-tête, pied de page, etc.).
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <title>Dashboard - NiceAdmin Bootstrap Template</title>
  <meta content="" name="description">
  <meta content="" name="keywords">
  <!-- Favicons -->
  <link href="assets/img/favicon.png" rel="icon">
  <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">
  <!-- Google Fonts -->
  <link href="https://fonts.gstatic.com" rel="preconnect">
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Nunito:300,300i,400,400i,600,600i,700,700i|Poppins:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">
    {% block css %}
    <!-- Vendor CSS Files -->
    <link rel="stylesheet" href="{{ url_for('static', filename='vendor/bootstrap/css/bootstrap.min.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='vendor/bootstrap-icons/bootstrap-icons.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='vendor/boxicons/css/boxicons.min.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='vendor/quill/quill.snow.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='vendor/quill/quill.bubble.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='vendor/remixicon/remixicon.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='vendor/simple-datatables/style.css') }}">
    <!-- Template Main CSS File -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    {% endblock %}
</head>
<body>
    {% block header %}
    <!-- ======= Header ======= -->
    <header id="header" class="header fixed-top d-flex align-items-center">
    <div class="d-flex align-items-center justify-content-between">
      <a href="index.html" class="logo d-flex align-items-center">
        <img src="assets/img/logo.png" alt="">
        <span class="d-none d-lg-block">NiceAdmin</span>
      </a>
      <i class="bi bi-list toggle-sidebar-btn"></i>
    </div><!-- End Logo -->
    <div class="search-bar">
      <form class="search-form d-flex align-items-center" method="POST" action="#">
        <input type="text" name="query" placeholder="Search" title="Enter search keyword">
        <button type="submit" title="Search"><i class="bi bi-search"></i></button>
      </form>
    </div><!-- End Search Bar -->
    <nav class="header-nav ms-auto">
      <ul class="d-flex align-items-center">
        <li class="nav-item d-block d-lg-none">
          <a class="nav-link nav-icon search-bar-toggle " href="#">
            <i class="bi bi-search"></i>
          </a>
        </li><!-- End Search Icon-->
        <li class="nav-item dropdown">
          <a class="nav-link nav-icon" href="#" data-bs-toggle="dropdown">
            <i class="bi bi-bell"></i>
            <span class="badge bg-primary badge-number">4</span>
          </a><!-- End Notification Icon -->
          <ul class="dropdown-menu dropdown-menu-end dropdown-menu-arrow notifications">
            <li class="dropdown-header">
              You have 4 new notifications
              <a href="#"><span class="badge rounded-pill bg-primary p-2 ms-2">View all</span></a>
            </li>
            <li>
              <hr class="dropdown-divider">
            </li>
            <li class="notification-item">
              <i class="bi bi-exclamation-circle text-warning"></i>
              <div>
                <h4>Lorem Ipsum</h4>
                <p>Quae dolorem earum veritatis oditseno</p>
                <p>30 min. ago</p>
              </div>
            </li>
            <li>
              <hr class="dropdown-divider">
            </li>
            <li class="notification-item">
              <i class="bi bi-x-circle text-danger"></i>
              <div>
                <h4>Atque rerum nesciunt</h4>
                <p>Quae dolorem earum veritatis oditseno</p>
                <p>1 hr. ago</p>
              </div>
            </li>
            <li>
              <hr class="dropdown-divider">
            </li>
            <li class="notification-item">
              <i class="bi bi-check-circle text-success"></i>
              <div>
                <h4>Sit rerum fuga</h4>
                <p>Quae dolorem earum veritatis oditseno</p>
                <p>2 hrs. ago</p>
              </div>
            </li>
            <li>
              <hr class="dropdown-divider">
            </li>
            <li class="notification-item">
              <i class="bi bi-info-circle text-primary"></i>
              <div>
                <h4>Dicta reprehenderit</h4>
                <p>Quae dolorem earum veritatis oditseno</p>
                <p>4 hrs. ago</p>
              </div>
            </li>
            <li>
              <hr class="dropdown-divider">
            </li>
            <li class="dropdown-footer">
              <a href="#">Show all notifications</a>
            </li>
          </ul><!-- End Notification Dropdown Items -->
        </li><!-- End Notification Nav -->
        <li class="nav-item dropdown">
          <a class="nav-link nav-icon" href="#" data-bs-toggle="dropdown">
            <i class="bi bi-chat-left-text"></i>
            <span class="badge bg-success badge-number">3</span>
          </a><!-- End Messages Icon -->
          <ul class="dropdown-menu dropdown-menu-end dropdown-menu-arrow messages">
            <li class="dropdown-header">
              You have 3 new messages
              <a href="#"><span class="badge rounded-pill bg-primary p-2 ms-2">View all</span></a>
            </li>
            <li>
              <hr class="dropdown-divider">
            </li>
            <li class="message-item">
              <a href="#">
                <img src="assets/img/messages-1.jpg" alt="" class="rounded-circle">
                <div>
                  <h4>Maria Hudson</h4>
                  <p>Velit asperiores et ducimus soluta repudiandae labore officia est ut...</p>
                  <p>4 hrs. ago</p>
                </div>
              </a>
            </li>
            <li>
              <hr class="dropdown-divider">
            </li>
            <li class="message-item">
              <a href="#">
                <img src="assets/img/messages-2.jpg" alt="" class="rounded-circle">
                <div>
                  <h4>Anna Nelson</h4>
                  <p>Velit asperiores et ducimus soluta repudiandae labore officia est ut...</p>
                  <p>6 hrs. ago</p>
                </div>
              </a>
            </li>
            <li>
              <hr class="dropdown-divider">
            </li>
            <li class="message-item">
              <a href="#">
                <img src="assets/img/messages-3.jpg" alt="" class="rounded-circle">
                <div>
                  <h4>David Muldon</h4>
                  <p>Velit asperiores et ducimus soluta repudiandae labore officia est ut...</p>
                  <p>8 hrs. ago</p>
                </div>
              </a>
            </li>
            <li>
              <hr class="dropdown-divider">
            </li>

            <li class="dropdown-footer">
              <a href="#">Show all messages</a>
            </li>
          </ul><!-- End Messages Dropdown Items -->
        </li><!-- End Messages Nav -->
        <li class="nav-item dropdown pe-3">
          <a class="nav-link nav-profile d-flex align-items-center pe-0" href="#" data-bs-toggle="dropdown">
            <!-- Afficher l'avatar -->
            {% if utilisateur[4] %}
                <img src="{{ url_for('static', filename='img/avatars/' + utilisateur[0]|string + '/' + utilisateur[4]) }}" alt="Profile" class="rounded-circle">
            {% else %}
                <p>Aucun avatar disponible.</p>
            {% endif %}
            <span class="d-none d-md-block dropdown-toggle ps-2">{{ utilisateur [1]}}</span>
          </a><!-- End Profile Iamge Icon -->
          <ul class="dropdown-menu dropdown-menu-end dropdown-menu-arrow profile">
            <li class="dropdown-header">
              <h6>Kevin Anderson</h6>
              <span>Web Designer</span>
            </li>
            <li>
              <hr class="dropdown-divider">
            </li>
            <li>
              <a class="dropdown-item d-flex align-items-center" href="/profile">
                <i class="bi bi-person"></i>
                <span>My Profile</span>
              </a>
            </li>
            <li>
              <hr class="dropdown-divider">
            </li>
            <li>
              <a class="dropdown-item d-flex align-items-center" href="users-profile.html">
                <i class="bi bi-gear"></i>
                <span>Account Settings</span>
              </a>
            </li>
            <li>
              <hr class="dropdown-divider">
            </li>
            <li>
              <a class="dropdown-item d-flex align-items-center" href="pages-faq.html">
                <i class="bi bi-question-circle"></i>
                <span>Need Help?</span>
              </a>
            </li>
            <li>
              <hr class="dropdown-divider">
            </li>
            <li>
              <a class="dropdown-item d-flex align-items-center" href="/deconnexion">
                <i class="bi bi-box-arrow-right"></i>
                <span>Sign Out</span>
              </a>
            </li>
          </ul><!-- End Profile Dropdown Items -->
        </li><!-- End Profile Nav -->
      </ul>
    </nav><!-- End Icons Navigation -->
    </header>
    <!-- End Header -->
    {% endblock %}
    <!-- ======= Sidebar ======= -->
    {% block sidebar %}
    <aside id="sidebar" class="sidebar">
    <ul class="sidebar-nav" id="sidebar-nav">
      <li class="nav-item">
        <a class="nav-link " href="index.html">
          <i class="bi bi-grid"></i>
          <span>Dashboard</span>
        </a>
      </li><!-- End Dashboard Nav -->
      <li class="nav-item">
        <a class="nav-link collapsed" data-bs-target="#components-nav" data-bs-toggle="collapse" href="#">
          <i class="bi bi-menu-button-wide"></i><span>Components</span><i class="bi bi-chevron-down ms-auto"></i>
        </a>
        <ul id="components-nav" class="nav-content collapse " data-bs-parent="#sidebar-nav">
          <li>
            <a href="components-alerts.html">
              <i class="bi bi-circle"></i><span>Alerts</span>
            </a>
          </li>
          <li>
            <a href="components-accordion.html">
              <i class="bi bi-circle"></i><span>Accordion</span>
            </a>
          </li>
          <li>
            <a href="components-badges.html">
              <i class="bi bi-circle"></i><span>Badges</span>
            </a>
          </li>
          <li>
            <a href="components-breadcrumbs.html">
              <i class="bi bi-circle"></i><span>Breadcrumbs</span>
            </a>
          </li>
          <li>
            <a href="components-buttons.html">
              <i class="bi bi-circle"></i><span>Buttons</span>
            </a>
          </li>
          <li>
            <a href="components-cards.html">
              <i class="bi bi-circle"></i><span>Cards</span>
            </a>
          </li>
          <li>
            <a href="components-carousel.html">
              <i class="bi bi-circle"></i><span>Carousel</span>
            </a>
          </li>
          <li>
            <a href="components-list-group.html">
              <i class="bi bi-circle"></i><span>List group</span>
            </a>
          </li>
          <li>
            <a href="components-modal.html">
              <i class="bi bi-circle"></i><span>Modal</span>
            </a>
          </li>
          <li>
            <a href="components-tabs.html">
              <i class="bi bi-circle"></i><span>Tabs</span>
            </a>
          </li>
          <li>
            <a href="components-pagination.html">
              <i class="bi bi-circle"></i><span>Pagination</span>
            </a>
          </li>
          <li>
            <a href="components-progress.html">
              <i class="bi bi-circle"></i><span>Progress</span>
            </a>
          </li>
          <li>
            <a href="components-spinners.html">
              <i class="bi bi-circle"></i><span>Spinners</span>
            </a>
          </li>
          <li>
            <a href="components-tooltips.html">
              <i class="bi bi-circle"></i><span>Tooltips</span>
            </a>
          </li>
        </ul>
      </li><!-- End Components Nav -->
      <li class="nav-item">
        <a class="nav-link collapsed" data-bs-target="#forms-nav" data-bs-toggle="collapse" href="#">
          <i class="bi bi-journal-text"></i><span>Forms</span><i class="bi bi-chevron-down ms-auto"></i>
        </a>
        <ul id="forms-nav" class="nav-content collapse " data-bs-parent="#sidebar-nav">
          <li>
            <a href="forms-elements.html">
              <i class="bi bi-circle"></i><span>Form Elements</span>
            </a>
          </li>
          <li>
            <a href="forms-layouts.html">
              <i class="bi bi-circle"></i><span>Form Layouts</span>
            </a>
          </li>
          <li>
            <a href="forms-editors.html">
              <i class="bi bi-circle"></i><span>Form Editors</span>
            </a>
          </li>
          <li>
            <a href="forms-validation.html">
              <i class="bi bi-circle"></i><span>Form Validation</span>
            </a>
          </li>
        </ul>
      </li><!-- End Forms Nav -->
      <li class="nav-item">
        <a class="nav-link collapsed" data-bs-target="#tables-nav" data-bs-toggle="collapse" href="#">
          <i class="bi bi-layout-text-window-reverse"></i><span>Tables</span><i class="bi bi-chevron-down ms-auto"></i>
        </a>
        <ul id="tables-nav" class="nav-content collapse " data-bs-parent="#sidebar-nav">
          <li>
            <a href="tables-general.html">
              <i class="bi bi-circle"></i><span>General Tables</span>
            </a>
          </li>
          <li>
            <a href="tables-data.html">
              <i class="bi bi-circle"></i><span>Data Tables</span>
            </a>
          </li>
        </ul>
      </li><!-- End Tables Nav -->
      <li class="nav-item">
        <a class="nav-link collapsed" data-bs-target="#charts-nav" data-bs-toggle="collapse" href="#">
          <i class="bi bi-bar-chart"></i><span>Charts</span><i class="bi bi-chevron-down ms-auto"></i>
        </a>
        <ul id="charts-nav" class="nav-content collapse " data-bs-parent="#sidebar-nav">
          <li>
            <a href="charts-chartjs.html">
              <i class="bi bi-circle"></i><span>Chart.js</span>
            </a>
          </li>
          <li>
            <a href="charts-apexcharts.html">
              <i class="bi bi-circle"></i><span>ApexCharts</span>
            </a>
          </li>
          <li>
            <a href="charts-echarts.html">
              <i class="bi bi-circle"></i><span>ECharts</span>
            </a>
          </li>
        </ul>
      </li><!-- End Charts Nav -->
      <li class="nav-item">
        <a class="nav-link collapsed" data-bs-target="#icons-nav" data-bs-toggle="collapse" href="#">
          <i class="bi bi-gem"></i><span>Icons</span><i class="bi bi-chevron-down ms-auto"></i>
        </a>
        <ul id="icons-nav" class="nav-content collapse " data-bs-parent="#sidebar-nav">
          <li>
            <a href="icons-bootstrap.html">
              <i class="bi bi-circle"></i><span>Bootstrap Icons</span>
            </a>
          </li>
          <li>
            <a href="icons-remix.html">
              <i class="bi bi-circle"></i><span>Remix Icons</span>
            </a>
          </li>
          <li>
            <a href="icons-boxicons.html">
              <i class="bi bi-circle"></i><span>Boxicons</span>
            </a>
          </li>
        </ul>
      </li><!-- End Icons Nav -->
      <li class="nav-heading">Pages</li>
      <li class="nav-item">
        <a class="nav-link collapsed" href="users-profile.html">
          <i class="bi bi-person"></i>
          <span>Profile</span>
        </a>
      </li><!-- End Profile Page Nav -->

      <li class="nav-item">
        <a class="nav-link collapsed" href="pages-faq.html">
          <i class="bi bi-question-circle"></i>
          <span>F.A.Q</span>
        </a>
      </li><!-- End F.A.Q Page Nav -->
      <li class="nav-item">
        <a class="nav-link collapsed" href="pages-contact.html">
          <i class="bi bi-envelope"></i>
          <span>Contact</span>
        </a>
      </li><!-- End Contact Page Nav -->
      <li class="nav-item">
        <a class="nav-link collapsed" href="pages-error-404.html">
          <i class="bi bi-dash-circle"></i>
          <span>Error 404</span>
        </a>
      </li><!-- End Error 404 Page Nav -->
    </ul>
    </aside>
    <!-- End Sidebar-->
    {% endblock %}
  <main id="main" class="main">
    {% block content %}{% endblock %}
  </main><!-- End #main -->
  <!-- ======= Footer ======= -->
  {% block footer %}
  <footer id="footer" class="footer">
    <div class="copyright">
      &copy; Copyright <strong><span>NiceAdmin</span></strong>. All Rights Reserved
    </div>
    <div class="credits">
      <!-- All the links in the footer should remain intact. -->
      <!-- You can delete the links only if you purchased the pro version. -->
      <!-- Licensing information: https://bootstrapmade.com/license/ -->
      <!-- Purchase the pro version with working PHP/AJAX contact form: https://bootstrapmade.com/nice-admin-bootstrap-admin-html-template/ -->
      Designed by <a href="https://bootstrapmade.com/">BootstrapMade</a>
    </div>
  </footer><!-- End Footer -->
  {% endblock %}
  <a href="#" class="back-to-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>
    {% block js %}
        <!-- Vendor JS Files -->
        <script src="{{ url_for('static', filename='vendor/apexcharts/apexcharts.min.js') }}"></script>
        <script src="{{ url_for('static', filename='vendor/bootstrap/js/bootstrap.bundle.min.js') }}"></script>
        <script src="{{ url_for('static', filename='vendor/chart.js/chart.umd.js') }}"></script>
        <script src="{{ url_for('static', filename='vendor/echarts/echarts.min.js') }}"></script>
        <script src="{{ url_for('static', filename='vendor/quill/quill.min.js') }}"></script>
        <script src="{{ url_for('static', filename='vendor/simple-datatables/simple-datatables.js') }}"></script>
        <script src="{{ url_for('static', filename='vendor/tinymce/tinymce.min.js') }}"></script>
        <script src="{{ url_for('static', filename='vendor/php-email-form/validate.js') }}"></script>
        <!-- Template Main JS File -->
        <script src="{{ url_for('static', filename='js/main.js') }}"></script>
    {% endblock %}
</body>
</html>
```
- Dans `base.html`, créez une mise en page de base avec les éléments communs à toutes les pages (en-tête, pied de page, etc.).
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <title>Pages / Register - NiceAdmin Bootstrap Template</title>
    <meta content="" name="description">
    <meta content="" name="keywords">
    <!-- Favicons -->
    <link href="assets/img/favicon.png" rel="icon">
    <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">
    <!-- Google Fonts -->
    <link href="https://fonts.gstatic.com" rel="preconnect">
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Nunito:300,300i,400,400i,600,600i,700,700i|Poppins:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">
    {% block css %}
    <!-- Vendor CSS Files -->
    <link rel="stylesheet" href="{{ url_for('static', filename='vendor/bootstrap/css/bootstrap.min.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='vendor/bootstrap-icons/bootstrap-icons.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='vendor/boxicons/css/boxicons.min.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='vendor/quill/quill.snow.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='vendor/quill/quill.bubble.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='vendor/remixicon/remixicon.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='vendor/simple-datatables/style.css') }}">
    <!-- Template Main CSS File -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    {% endblock %}
</head>
    <body>
        <main>
            <div class="container">
                {% block content %}{% endblock %}
            </div>
        </main>
        <a href="#" class="back-to-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>
        {% block js %}
            <!-- Vendor JS Files -->
            <script src="{{ url_for('static', filename='vendor/apexcharts/apexcharts.min.js') }}"></script>
            <script src="{{ url_for('static', filename='vendor/bootstrap/js/bootstrap.bundle.min.js') }}"></script>
            <script src="{{ url_for('static', filename='vendor/chart.js/chart.umd.js') }}"></script>
            <script src="{{ url_for('static', filename='vendor/echarts/echarts.min.js') }}"></script>
            <script src="{{ url_for('static', filename='vendor/quill/quill.min.js') }}"></script>
            <script src="{{ url_for('static', filename='vendor/simple-datatables/simple-datatables.js') }}"></script>
            <script src="{{ url_for('static', filename='vendor/tinymce/tinymce.min.js') }}"></script>
            <script src="{{ url_for('static', filename='vendor/php-email-form/validate.js') }}"></script>
            <!-- Template Main JS File -->
            <script src="{{ url_for('static', filename='js/main.js') }}"></script>
        {% endblock %}
    </body>
</html>
```
Créez un fichier **templates /index.html** avec le contenu suivant :
```html
{% extends "base.html" %}

{% block content %}
    <section class="section register min-vh-100 d-flex flex-column align-items-center justify-content-center py-4">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-4 col-md-6 d-flex flex-column align-items-center justify-content-center">
                    <!-- Logo Component -->
                    {% include 'components/logo.html' %}

                    <div class="card mb-3">
                        <div class="card-body">
                            <!-- Registration Form Component -->
                            {% include 'components/registration_form.html' %}
                        </div>
                    </div>

                    <div class="credits">
                        <!-- Credits content here -->
                    </div>
                </div>
            </div>
        </div>
    </section>
{% endblock %}
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








