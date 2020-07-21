#Project Flask MVC

__author__ = "oswscript"
__version__ = "0"
__email__ = "oswscript@gmail.com"

from inventario import app

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
