from wtforms import Form, Field
from wtforms import StringField, PasswordField
from inventario.helpers.custom_validations import *

class SignupForm(Form):

    #input name
    name = StringField('Name',
    [
        valid_no_empty
    ],
    render_kw={"placeholder": "Name"}
    )

    #input username
    username = StringField('Username',
    [
        valid_limit,
        valid_no_empty
    ],
    
    render_kw={"placeholder": "Username"}
    )

    #input email
    email = StringField('Email',
    [
        valid_limit,
        valid_no_empty
    ],
    
    render_kw={"placeholder": "Emails"}
    )

    #input password
    password = PasswordField('Password',[
        valid_no_empty,
        validators.Length(min=6,message="Password must be at least 6 characters"),
        validators.EqualTo('confirm', message='Password no match')


    ], 
    render_kw={"placeholder": "Password"}
    )

    #input confirm password
    confirm = PasswordField('Confirm',render_kw={"placeholder": "Confirm Password"})
