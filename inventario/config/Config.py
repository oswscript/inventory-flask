import inventario.config.Database as db

class Config(object):
  SECRET_KEY = 'oswscript-clave-secreta'
  SERVER_NAME = "localhost:8000"
  #SQLALCHEMY_DATABASE_URI = db.db_type+'://'+db.user+':'+db.password+'@'+db.host+'/'+db.db_name
  
  SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost:5432/pruebaflask'


  #SQLALCHEMY_DATABASE_URI = 'postgresql://lamanzan:zN0Nn*cfH@HEowQ@localhost:5432/lamanzan_practicaflask'
  SQLALCHEMY_TRACK_MODIFICATIONS = False

class Dev(Config):
  DEBUG = True
  
class Prod(Config):
  DEBUG = False
