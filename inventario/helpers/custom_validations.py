""" CUSTOM VALIDATIONS """

#character limit of username
def valid_username_limit(form,field):
    if len(field.data) < 3:

        raise validators.ValidationError("Username must be at least 3 characters")

    elif len(field.data) > 20:

        raise validators.ValidationError("The username must have a maximum of 3 characters")
    
    else:

        raise validators.ValidationError("ok")

