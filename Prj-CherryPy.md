# Fiche d'Activité Pratique : Création d'un Petit Projet avec CherryPy
## Objectif
L'objectif de cette activité pratique est de créer un projet Web simple en utilisant le framework CherryPy en Python. À la fin de cette activité, les participants auront mis en place un serveur Web basique avec quelques pages.
## Prérequis
* Python installé sur la machine
* Connaissance de base en programmation Python
## Étapes
**Étape 1: Installation de CherryPy**
Assurez-vous que CherryPy est installé en exécutant la commande suivante dans votre terminal ou invite de commande :
```bash
pip install cherrypy
```
**Étape 2: Structure du Projet**
Créez un dossier pour votre projet. À l'intérieur, créez les fichiers suivants :
* app.py : Le script principal de l'application CherryPy.
* templates/ : Un dossier pour stocker les fichiers HTML.

**Étape 3: Configuration de l'Application**
Ouvrez le fichier app.py et ajoutez le code suivant pour configurer une application Web simple avec CherryPy :
```python
import cherrypy

class HelloWorld:
    @cherrypy.expose
    def index(self):
        return "Bonjour, ceci est la page d'accueil!"

if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())

```
**Étape 4: Ajout de Pages HTML**
Créez un fichier HTML dans le dossier templates/. Par exemple, index.html :

**Étape 5: Intégration des Pages HTML**
Modifiez la méthode index dans app.py pour renvoyer le contenu du fichier HTML :

**Étape 6: Exécution de l'Application**
Exécutez l'application en lançant le script app.py. Ouvrez votre navigateur et accédez à http://localhost:8080 pour voir le résultat.

## Conclusion
Félicitations ! Vous avez créé un petit projet Web avec CherryPy en Python. Explorez davantage CherryPy pour ajouter des fonctionnalités supplémentaires à votre application.

