from wtforms import Form, Field
from wtforms import StringField, validators, PasswordField
from inventario.helpers.custom_validations import valid_username_limit

class LoginForm(Form):
    username = StringField(
    [
        valid_username_limit
    ],
    render_kw={"placeholder": "Username"}
    )

    password = PasswordField([
        validators.DataRequired(),
    ], 
    render_kw={"placeholder": "Password"}
    )