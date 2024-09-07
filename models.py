from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    legajo = db.Column(db.Integer, primary_key=True)  # Clave primaria
    nombre = db.Column(db.String(255), nullable=False)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    usuario = db.Column(db.String(255), unique=True, nullable=False)
    contrasena = db.Column(db.String(255), nullable=False)
    tipo_usuario = db.Column(db.String(50), nullable=False)
    rol = db.Column(db.String(50), nullable=False, default='usuario')  # Nuevo campo para roles
    # Método para hashear la contraseña
    def set_password(self, password):
        self.contrasena = generate_password_hash(password)
    
    # Método para verificar la contraseña
    def check_password(self, password):
        return check_password_hash(self.contrasena, password)

    # Método que devuelve el identificador del usuario
    def get_id(self):
        return str(self.legajo)  # Devuelve el legajo como identificador del usuario

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # 'Ingreso' o 'Egreso'

class MetodoPago(db.Model):
    __tablename__ = 'metodopago'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)

class Ingreso(db.Model):
    __tablename__ = 'ingresos'
    codigo = db.Column(db.Integer, primary_key=True)
    idcategoria = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    categoria = db.relationship('Categoria', backref='ingresos')  # Relación con Categoria
    legajousuario = db.Column(db.Integer, db.ForeignKey('usuarios.legajo'), nullable=False)
    descripcion = db.Column(db.String(255))
    fecha = db.Column(db.Date, default=datetime.utcnow)
    hora = db.Column(db.Time, default=datetime.utcnow)
    importe = db.Column(db.Float, nullable=False)

class Egreso(db.Model):
    __tablename__ = 'egresos'
    codigo = db.Column(db.Integer, primary_key=True)
    idcategoria = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    categoria = db.relationship('Categoria', backref='egresos')  # Relación con Categoria
    legajousuario = db.Column(db.Integer, db.ForeignKey('usuarios.legajo'), nullable=False)
    descripcion = db.Column(db.String(255))
    fecha = db.Column(db.Date, default=datetime.utcnow)
    hora = db.Column(db.Time, default=datetime.utcnow)
    destinatario = db.Column(db.String(255))
    importe = db.Column(db.Float, nullable=False)
    impuestos = db.Column(db.Float)
    idMetodoPago = db.Column(db.Integer, db.ForeignKey('metodopago.id'), nullable=False)
