"""MODULES FLASK"""
from inventario import app
from flask import render_template, redirect, url_for

"""HELPERS"""
from inventario.helpers import form

"""
    Import MOdels
from project.models.HelloController import Hello
"""
#route index
@app.route('/', methods = ['GET'])
def index():
    title = 'Login'
    data = {
        "title": form.helperTest(),
        "body": "Flask simple MVC"
    }
    return render_template('auth/index.html.j2',title = title, data = data)
