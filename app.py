from flask import Flask
from extensions import db, migrate, login_manager
from config import Config
from admin.views import initialize_admin  # Importar la configuración del panel de admin
from routes.history import history_bp
from extensions import db
app = Flask(__name__)

# Configurar la base de datos y otras configuraciones
app.config.from_object(Config)
# Asegúrate de registrar el blueprint en tu aplicación
app.register_blueprint(history_bp)

# Inicializar las extensiones
db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Inicializa el panel de administración
initialize_admin(app)

# Importar y registrar Blueprints
from routes.auth import auth_bp
from routes.transactions import transactions_bp
from routes.dashboard import dashboard_bp

app.register_blueprint(auth_bp)
app.register_blueprint(transactions_bp)
app.register_blueprint(dashboard_bp)

if __name__ == '__main__':
    app.run(debug=True)
