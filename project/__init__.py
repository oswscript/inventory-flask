from flask import Flask

app = Flask("project", template_folder='templates', static_folder='static')

from project.controllers import *
