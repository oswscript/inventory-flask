"""MODULES FLASK"""
from inventario import app
from flask import render_template, redirect, url_for, request, session, flash
import inventario.forms.LoginForm as form

@app.errorhandler(404)
def error_404(e):
    return "Not found 404"

@app.before_request
def before_request():
    
    if 'user' not in session and request.endpoint in ['dash']:
        
        flash('You cannot enter this site without logging in', 'warning')
        return redirect(url_for('login'))
        
    elif 'user' in session and request.endpoint in ['login','signup']:

        return redirect(url_for('dash'))

#route index
@app.route('/dash', methods = ['GET','POST'])
def dash():
    
    title = 'Dashboard'

    return render_template('dash.html.j2')
