import datetime
from inventario import db 
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel(db.Model):

  #nombre tabla
  __tablename__ = 'users'

  #columns
  id = db.Column(db.Integer, primary_key=True)
  name= db.Column(db.String(80), nullable=True)
  username= db.Column(db.String(80), unique=True, nullable=True)
  email = db.Column(db.String(256), unique=True, nullable=True)
  password = db.Column(db.String(128), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.now)
  
  #init data
  def __init__(self, name, username, email, password):

    #declare data
    self.name = name
    self.username = username
    self.email = email
    self.password = self.create_password(password)

  #Generate Hash password
  def create_password(self, password):
    return generate_password_hash(password)

  #Verifique hash password
  def verify_password(self, password):
    return check_password_hash(self.password, password)
