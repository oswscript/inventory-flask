"""MODULES FLASK"""
from inventario import app
from flask import render_template, redirect, url_for, request
import inventario.forms.LoginForm as form

"""HELPERS"""

"""
    Import MOdels
from project.models.HelloController import Hello
"""
#route index
@app.route('/', methods = ['GET','POST'])
def index():
    title = 'Login'
    login_form = form.LoginForm(request.form)
    data = {
        "title": "dsdf",
        "body": "Flask simple MVC"
    }
    return render_template('auth/index.html.j2',title = title, data = data, form = login_form)
