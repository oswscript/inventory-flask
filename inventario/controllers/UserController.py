"""MODULES FLASK"""
from inventario import app, db
from flask import render_template, redirect, url_for, request, session, flash
from werkzeug.security import generate_password_hash

"""FORMS"""
import inventario.forms.SignupForm as sform
import inventario.forms.UpdateUserForm as Uform
import inventario.forms.UpdatePassForm as UPform

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
@app.route('/users', methods = ['GET'])
def index_users():

    title = 'Users list'

    #get all
    users = User.query.all()

    return render_template('users/index.html.j2',title = title, users = users)


#route create
@app.route('/createuser', methods = ['GET','POST'])
def create_users():

    title = 'Create users'
    signup_form= sform.SignupForm(request.form)

    #get all
    users = User.query.all()

    if request.method == 'POST' and signup_form.validate():

        check_username = User.query.filter_by(username = signup_form.username.data).scalar()
        check_email = User.query.filter_by(email = signup_form.email.data).scalar()

        if check_username is not None:

            msj = "Username already exists."

            flash(msj,"danger")
            
            return render_template('users/create.html.j2',title = title, form = signup_form)
        
        elif check_email is not None:

            msj = "Email already exists."

            flash(msj,"danger")
            
            return render_template('users/create.html.j2',title = title, form = signup_form)

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

            return render_template('users/index.html.j2',title = title, users = users)

    else:
        return render_template('users/create.html.j2',title = title, form = signup_form)


@app.route('/updateuser/<int:id>', methods=['GET','POST'])
def update_user(id):

    title = 'Update user'
    data = User.query.get(id)
    form = Uform.UpdateUserForm(request.form)
    
    if request.method == 'POST' and form.validate():

        data = User.query.filter_by(id = id).first()
        data.fullname = form.fullname.data
        data.username = form.username.data
        data.email = form.email.data
        db.session.add(data)
        db.session.commit()

        flash('Updated user data', 'success')
        return redirect( url_for('index_users') )

    else:
        return render_template('users/update.html.j2', id= id, title = title, data = data, form = form)



@app.route('/update_pass_user/<int:id>', methods=['GET','POST'])
def update_pass_user(id):

    title = 'Update user'
    data = User.query.get(id)
    form = UPform.UpdatePasswordForm(request.form)
    
    if request.method == 'POST' and form.validate():

        data = User.query.filter_by(id = id).first()
        data.password = generate_password_hash(form.password.data)
        db.session.add(data)
        db.session.commit()

        flash('Updated password correct', 'success')
        return redirect( url_for('index_users') )

    else:
        return render_template('users/update_pass.html.j2', id= id, title = title, data = data, form = form)


@app.route('/deleteuser/<int:id>', methods=['GET'])
def delete_user(id):
    
    data = User.query.filter_by(id = id).first()

    db.session.delete(data)
    db.session.commit()

    flash("User delete succefull", 'success')
    return redirect( url_for('index_users') )
