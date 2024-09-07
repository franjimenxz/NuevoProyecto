from flask import Flask
from extensions import db, migrate, login_manager
from config import Config
app = Flask(__name__)

# Configurar la base de datos y otras configuraciones
app.config.from_object(Config)

# Inicializar las extensiones
db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Importar y registrar Blueprints
from routes.auth import auth_bp
from routes.transactions import transactions_bp
from routes.dashboard import dashboard_bp

app.register_blueprint(auth_bp)
app.register_blueprint(transactions_bp)
app.register_blueprint(dashboard_bp)

if __name__ == '__main__':
    app.run(debug=True)
