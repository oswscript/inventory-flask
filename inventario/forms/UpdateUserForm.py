from wtforms import Form, Field
from wtforms import StringField, PasswordField
from inventario.helpers.custom_validations import *

class UpdateUserForm(Form):

    #input name
    fullname = StringField('Fullname',
    [
        valid_no_empty,
    ],
    render_kw={"placeholder": "Fullname"}
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
        valid_no_empty
    ],
    
    render_kw={"placeholder": "Email"}
    )
