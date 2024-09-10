from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import Select2Widget
from flask_login import current_user
from wtforms import SelectField
from models import Usuario, Categoria, MetodoPago
from extensions import db

# Clase personalizada para proteger el acceso al panel de administración
class AdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.rol == 'admin'  # Verifica que sea admin

# Clase personalizada para el modelo Usuario para incluir el campo 'rol' como un SelectField
class UsuarioAdminView(AdminView):
    # Sobrescribimos el formulario para el campo 'rol'
    form_overrides = {
        'rol': SelectField
    }

    # Definimos las opciones que aparecerán en el campo SelectField para el rol
    form_args = {
        'rol': {
            'choices': [('usuario', 'Usuario'), ('admin', 'Admin')]
        }
    }

def initialize_admin(app):
    # Inicializa Flask-Admin
    admin = Admin(app, name='Admin Panel', template_mode='bootstrap4')

    # Agrega los modelos que quieres gestionar en el panel de administración
    admin.add_view(UsuarioAdminView(Usuario, db.session))
    admin.add_view(AdminView(Categoria, db.session))
    admin.add_view(AdminView(MetodoPago, db.session))
