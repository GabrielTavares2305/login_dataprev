from app import app
from flask import render_template, url_for, request
from app.forms import CadastroForm

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/login/')
def loginpage():
    return render_template('login.html')

@app.route('/cadastro/', methods=['GET', 'POST'])
def signinpage():
    form = CadastroForm()
    context = {}

    return render_template('cadastro.html', context=context, form=form)





