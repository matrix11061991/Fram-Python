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
