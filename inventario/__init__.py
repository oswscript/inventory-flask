from flask import Flask
from flask_wtf import CSRFProtect
from inventario.config.Config import Dev, Prod
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

app = Flask("inventario", template_folder='templates', static_folder='static')
app.config.from_object(Dev)
csrf = CSRFProtect()

from inventario.controllers import *
