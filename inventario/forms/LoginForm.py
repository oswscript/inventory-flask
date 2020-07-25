from wtforms import Form, Field
from wtforms import StringField, PasswordField
from inventario.helpers.custom_validations import *

class LoginForm(Form):
    username = StringField('Username',
    [
        valid_limit,
        valid_no_empty
    ],
    render_kw={"placeholder": "Username"}
    )

    password = PasswordField('Password',[
        valid_no_empty,
        validators.Length(min=6,message="Password must be at least 6 characters"),

    ], 
    render_kw={"placeholder": "Password"}
    )