#Proyecto de Gestión Financiera Web
Este proyecto es una aplicación web de gestión financiera que permite a los usuarios registrar y gestionar sus ingresos y egresos, con el objetivo de tener un control completo sobre sus finanzas personales. La aplicación también permite a los administradores gestionar a los usuarios a través de un panel de administración.

##Funcionalidades Principales
1. Registro e inicio de sesión de usuarios:
Los usuarios pueden registrarse con un nombre de usuario, nombre completo, DNI, y contraseña.
Luego, pueden iniciar sesión para acceder a sus datos financieros.
Se utiliza Flask-Login para la autenticación de usuarios.
2. Gestión de transacciones:
Los usuarios pueden registrar tanto ingresos como egresos.
Cada transacción puede estar categorizada (ej. Salario, Alquiler, Compras, etc.).
Los egresos, además, incluyen la opción de seleccionar un método de pago.
3. Dashboard personal:
Cada usuario tiene un dashboard donde puede visualizar un resumen de sus ingresos, egresos y saldo actual.
El dashboard incluye gráficos generados con Chart.js para representar los ingresos y egresos por categoría, así como un balance general.
Los datos pueden ser filtrados por día, permitiendo a los usuarios visualizar transacciones específicas por fechas.
4. Gestión por administrador:
Los administradores pueden gestionar a los usuarios desde un panel de administración utilizando Flask-Admin.
Los administradores pueden agregar, editar o eliminar usuarios, así como ver sus transacciones.
5. Panel de administración:
El acceso a este panel está restringido solo para administradores.
Los administradores pueden gestionar usuarios y modificar sus roles.
#Tecnologías Utilizadas

##Backend:
Flask: Framework para el desarrollo web.
Flask-Login: Manejo de autenticación y sesión de usuarios.
Flask-Migrate: Manejo de migraciones de base de datos.
SQLAlchemy: ORM para manejar las interacciones con PostgreSQL.

##Frontend:
HTML5, CSS3 y Bootstrap: Para el diseño de la interfaz.
Chart.js: Para generar gráficos interactivos en el dashboard.

##Base de Datos:
PostgreSQL: Sistema de gestión de bases de datos relacional.

#Instalación y Configuración
##1. Clonar el repositorio 
git clone https://github.com/usuario/proyecto-finanzas.git
cd proyecto-finanzas

##2. Crear un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

##3. Instalar las dependencias
pip install -r requirements.txt

##4. Configurar la base de datos
Crea una base de datos en PostgreSQL para el proyecto. Luego, configura el archivo config.py con las credenciales de tu base de datos:
SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/nombre_db'

##5. Migraciones de base de datos
Para aplicar las migraciones iniciales de la base de datos, ejecuta los siguientes comandos: 
flask db init
flask db migrate -m "Migración inicial"
flask db upgrade

##6. Cargar usuario administrador
Para asignar el rol de administrador a un usuario, debes acceder a la base de datos y actualizar manualmente el campo rol a 'admin' para el usuario deseado.

##7. Ejecutar la aplicación
Finalmente, ejecuta la aplicación localmente:
flask run
La aplicación estará disponible en http://127.0.0.1:5000/.

##Estructura del Proyecto

project/
│
├── app.py               # Archivo principal de la aplicación Flask.
├── config.py            # Configuración de la aplicación.
├── extensions.py        # Inicialización de las extensiones (db, login_manager, etc.).
├── models.py            # Definición de los modelos de la base de datos.
├── forms.py             # Definición de los formularios.
├── routes/
│   ├── auth.py          # Rutas de autenticación (registro, login).
│   ├── dashboard.py     # Rutas para el dashboard de usuario.
│   ├── transactions.py  # Rutas para manejar transacciones (ingresos/egresos).
│   └── admin.py         # Rutas para el panel de administración.
├── migrations/          # Directorio de migraciones de base de datos.
├── templates/           # Directorio de templates HTML.
│   ├── base.html        # Template base.
│   ├── dashboard.html   # Template del dashboard.
│   ├── add_transaction.html  # Template para agregar transacciones.
│   └── ...              # Otros templates.
└── static/              # Archivos estáticos como CSS y JS.
    ├── styles.css       # Archivo de estilos CSS.
    └── ...
#Funcionalidades Futuras
Agregar la funcionalidad de exportar datos a CSV o Excel.
Implementar reportes financieros avanzados (gráficos de tendencias, predicciones).
Integrar con APIs de pagos para automatizar los registros de transacciones.
