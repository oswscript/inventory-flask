"""MODULES FLASK"""
from inventario import app
from flask import render_template, redirect, url_for, request, session, flash
import inventario.forms.LoginForm as form

"""DATABASES"""
from inventario.models.UserModel import UserModel as User
#route index
@app.route('/', methods = ['GET','POST'])
def index():
    title = 'Login'
    login_form = form.LoginForm(request.form)

    if request.method == 'POST' and login_form.validate():

        username = login_form.username.data
        password = login_form.password.data

        #check username
        user = User.query.filter_by(username = username).first()

        if user is not None:

            if user.verify_password(password):

                session['usr'] = user.username
                session['usr_id'] = user.id
                msj = "Conectado con exito"
                flash(msj,"success")
                return render_template('dash.html.j2', title = "Dashboard")
                
            else:
                
                msj = "Datos incorrectos"
                flash(msj,"danger")
                
            return render_template('auth/index.html.j2',title = title, form = login_form)

        else:

            msj = "Usuario no existe"
            flash(msj,"danger")
            return render_template('auth/index.html.j2',title = title, form = login_form)


    else:
        return render_template('auth/index.html.j2',title = title, form = login_form)

@app.route('/signup', methods = ['GET','POST'])
def signup():
    title = 'Sign Up'
    login_form = form.LoginForm(request.form)

    if request.method == 'POST' and login_form.validate():

        #return redirect( url_for('dash') )
        if login_form.validate():

            #Datos se sesion
            session['username'] = "oswscript"
            session['user_id'] = 100
            session['user_email'] = "oswscript@gmail.com"
            session['user_rol'] = "admin"

            #mensaje flash
            msj = "Conectado con exito"
            flash(msj,"success")

            return redirect( url_for('dash') )

        else:
            return "false"

    else:
        return render_template('auth/index.html.j2',title = title, form = login_form)
