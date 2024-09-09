import os

class Config:
    # Configuración básica
    SECRET_KEY = os.getenv('SECRET_KEY', 'clave_secreta')

    # Configuración de la base de datos PostgreSQL
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:TheLegends123@localhost/GestionFina'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
