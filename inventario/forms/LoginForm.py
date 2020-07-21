from wtforms import Form, Field
from wtforms import StringField, validators, PasswordField
from helpers import custom_validations

class LoginForm(Form):
    username = StringField('Username', 
    [
        custom_validations.valid_username_limit
    ])
