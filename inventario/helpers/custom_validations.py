""" CUSTOM VALIDATIONS """
from wtforms import validators

#character limit
def valid_limit(form,field):
    
    if len(field.data) > 0 and len(field.data) < 3:

        raise validators.ValidationError("The "+field.name.title()+" must be at least 3 characters")

    elif len(field.data) > 10:

        raise validators.ValidationError("The "+field.name.title()+" must have a maximum of 10 characters")


def valid_no_empty(form,field):

    if(len(field.data) == 0):

        raise validators.ValidationError(field.name.title()+" field is required")
    

    