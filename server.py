"""
;==========================================
; Title:  Iventory System
; Author: @oswscript
; Date:   21 July 2020
; Version: 0
;==========================================

"""
__author__ = "oswscript"
__version__ = "0"
__email__ = "oswscript@gmail.com"

from inventario import app
from inventario import csrf
from inventario import db

if __name__ == '__main__':

    #Config and load CSRF
    csrf.init_app(app)
    
    #init db
    db.init_app(app)
    with app.app_context():
        db.create_all()

    #Run
    app.run()
