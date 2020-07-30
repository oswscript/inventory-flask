from flask import Flask
from flask_wtf import CSRFProtect
from inventario.config.Config import Dev, Prod
from flask_sqlalchemy import SQLAlchemy
from logging import FileHandler, WARNING
db = SQLAlchemy()

app = Flask("inventario", template_folder='templates', static_folder='static')
app.config.from_object(Dev)
csrf = CSRFProtect()

#capture error
if not app.debug:
    file_handler = FileHandler('errorlog.txt')
    file_handler.setLevel(WARNING)

    app.logger.addHandler(file_handler)

from inventario.controllers import *
