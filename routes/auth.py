from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from forms import RegisterForm, LoginForm
from models import Usuario
from extensions import db, login_manager  # Cambia esto
from sqlalchemy.exc import IntegrityError


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        nuevo_usuario = Usuario(
            usuario=form.usuario.data,
            nombre=form.nombre.data,
            dni=form.dni.data,
            tipo_usuario='usuario'
        )
        nuevo_usuario.set_password(form.contrasena.data)
        db.session.add(nuevo_usuario)
        try:
            db.session.commit()
            flash('Usuario registrado exitosamente', 'success')
            return redirect(url_for('auth.login'))
        except IntegrityError:
            db.session.rollback()
            flash('El usuario o DNI ya existen. Por favor, elige otros.', 'register_error')

    return render_template('register.html', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Lógica de autenticación
        user = Usuario.query.filter_by(usuario=form.usuario.data).first()
        if user is None or not user.check_password(form.contrasena.data):
            flash('Usuario o contraseña incorrectos', 'login_error')
            return redirect(url_for('auth.login'))

        # Si el login es exitoso
        login_user(user)
        return redirect(url_for('dashboard.index'))

    return render_template('login.html', form=form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# Registrar la función user_loader
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))  # Cargar el usuario por ID
