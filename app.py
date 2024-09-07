from flask import Flask
from extensions import db, migrate, login_manager
from config import Config
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from models import Usuario, Categoria, MetodoPago  # Importa tus modelos

app = Flask(__name__)

# Configurar la base de datos y otras configuraciones
app.config.from_object(Config)

# Inicializar las extensiones
db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Clase personalizada para proteger el acceso al panel de administración
class AdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.rol == 'admin'  # Verifica que sea admin

# Inicializa Flask-Admin
admin = Admin(app, name='Admin Panel', template_mode='bootstrap4')

# Agrega los modelos que quieres gestionar en el panel de administración
admin.add_view(AdminView(Usuario, db.session))
admin.add_view(AdminView(Categoria, db.session))
admin.add_view(AdminView(MetodoPago, db.session))

# Importar y registrar Blueprints
from routes.auth import auth_bp
from routes.transactions import transactions_bp
from routes.dashboard import dashboard_bp

app.register_blueprint(auth_bp)
app.register_blueprint(transactions_bp)
app.register_blueprint(dashboard_bp)

if __name__ == '__main__':
    app.run(debug=True)
