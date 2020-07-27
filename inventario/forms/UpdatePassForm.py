from wtforms import Form, Field
from wtforms import StringField, PasswordField
from inventario.helpers.custom_validations import *

class UpdatePasswordForm(Form):

    #input password
    password = PasswordField('Password',[
        valid_no_empty,
        validators.Length(min=6,message="Password must be at least 6 characters"),
        validators.EqualTo('confirm_pass', message='Password no match')


    ], 
    render_kw={"placeholder": "Password"}
    )

    #input confirm password
    confirm_pass = PasswordField('Confirm', render_kw={'placeholder':'Confirm password'})
