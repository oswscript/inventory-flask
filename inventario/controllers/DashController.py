"""MODULES FLASK"""
from inventario import app
from flask import render_template, redirect, url_for, request, session, flash
import inventario.forms.LoginForm as form

"""HELPERS"""

"""
    Import MOdels
from project.models.HelloController import Hello
"""
#route index
@app.route('/dash', methods = ['GET','POST'])
def dash():
    title = 'Dashboard'
  
    return render_template('dash.html.j2')
