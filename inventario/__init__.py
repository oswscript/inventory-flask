from flask import Flask

app = Flask("inventario", template_folder='templates', static_folder='static')

from inventario.controllers import *
