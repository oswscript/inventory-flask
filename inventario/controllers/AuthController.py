"""MODULES FLASK"""
from inventario import app, db
from flask import render_template, redirect, url_for, request, session, flash

"""FORMS"""
import inventario.forms.LoginForm as lform
import inventario.forms.SignupForm as sform

"""DATABASES"""
from inventario.models.UserModel import UserModel as User

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
@app.route('/', methods = ['GET','POST'])
def login():
    title = 'Login'
    login_form = lform.LoginForm(request.form)

    if request.method == 'POST' and login_form.validate():

        username = login_form.username.data
        password = login_form.password.data

        #check username
        check_username = User.query.filter_by(username = login_form.username.data).scalar()

        #capture user data
        user = User.query.filter_by(username = username).first()

        if check_username is not None:

            if user.verify_password(password):

                session['user'] = user.username
                session['user_id'] = user.id
                session['user_email'] = user.email

                msj = "Has successfully connected"
                flash(msj,"success")
                return redirect(url_for('dash'))
                
            else:
                
                msj = "Incorrect data, try again"
                flash(msj,"danger")
                
            return render_template('auth/login.html.j2',title = title, form = login_form)

        else:

            msj = "This user does not exist"
            flash(msj,"danger")
            return render_template('auth/login.html.j2',title = title, form = login_form)


    else:
        return render_template('auth/login.html.j2',title = title, form = login_form)

@app.route('/signup', methods = ['GET','POST'])
def signup():
    
    title = 'Sign Up'
    signup_form= sform.SignupForm(request.form)
    login_form = lform.LoginForm(request.form)

    if request.method == 'POST' and signup_form.validate():

        check_username = User.query.filter_by(username = signup_form.username.data).scalar()
        check_email = User.query.filter_by(email = signup_form.email.data).scalar()

        if check_username is not None:

            msj = "Username already exists."

            flash(msj,"danger")
            
            return render_template('auth/signup.html.j2',title = title, form = signup_form)
        
        elif check_email is not None:

            msj = "Email already exists."

            flash(msj,"danger")
            
            return render_template('auth/signup.html.j2',title = title, form = signup_form)

        else:

            #database record
            data = User(

                fullname = signup_form.fullname.data,
                username = signup_form.username.data,
                email = signup_form.email.data,
                password = signup_form.password.data

            )
            db.session.add(data)
            db.session.commit()
            #end database record

            msj = "Registro exitoso."
            flash(msj,"success")

            return render_template('auth/login.html.j2',title = title, form = login_form)

    else:

        return render_template('auth/signup.html.j2',title = title, form = signup_form)


@app.route('/logout')
def logout():

    if 'user' in session:
        session.pop('user')
        msj = "You have disconnected"
        flash(msj,"success")

    return redirect(url_for('login'))