from flask import Blueprint, render_template, redirect, url_for, flash
from forms import TransactionForm
from models import Ingreso, Egreso, Categoria, MetodoPago
from extensions import db
from flask_login import current_user, login_required

transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route('/add_income', methods=['GET', 'POST'])
@login_required  # Asegúrate de que el usuario esté autenticado
def add_income():
    form = TransactionForm()

    # Cargar categorías de ingreso
    form.idcategoria.choices = [(c.id, c.nombre) for c in Categoria.query.filter_by(tipo='Ingreso').all()]

    # Eliminamos el campo de método de pago en los ingresos
    del form.idmetodopago

    if form.validate_on_submit():
        try:
            print("Formulario de ingreso validado correctamente.")
            nuevo_ingreso = Ingreso(
                descripcion=form.descripcion.data,
                importe=form.importe.data,
                idcategoria=form.idcategoria.data,
                legajousuario=current_user.legajo  # Asegúrate de tener el usuario actual
            )
            db.session.add(nuevo_ingreso)
            db.session.commit()
            flash('Ingreso agregado correctamente', 'success')
            print(f"Ingreso agregado: {nuevo_ingreso}")
            return redirect(url_for('dashboard.index'))
        except Exception as e:
            db.session.rollback()
            flash('Error al agregar el ingreso', 'danger')
            print(f"Error al agregar el ingreso: {e}")
    else:
        print("Validación fallida:", form.errors)

    return render_template('add_transaction.html', form=form, tipo_transaccion='Ingreso')

@transactions_bp.route('/add_expense', methods=['GET', 'POST'])
@login_required  # Asegúrate de que el usuario esté autenticado
def add_expense():
    form = TransactionForm()

    # Cargar categorías de egreso
    form.idcategoria.choices = [(c.id, c.nombre) for c in Categoria.query.filter_by(tipo='Egreso').all()]

    # Cargar los métodos de pago
    form.idmetodopago.choices = [(m.id, m.nombre) for m in MetodoPago.query.all()]

    if form.validate_on_submit():
        try:
            print("Formulario de egreso validado correctamente.")
            nuevo_egreso = Egreso(
                descripcion=form.descripcion.data,
                importe=form.importe.data,
                idcategoria=form.idcategoria.data,
                idMetodoPago=form.idmetodopago.data,
                legajousuario=current_user.legajo  # Usar el campo correcto para el usuario
            )
            db.session.add(nuevo_egreso)
            db.session.commit()
            flash('Egreso agregado correctamente', 'success')
            print(f"Egreso agregado: {nuevo_egreso}")
            return redirect(url_for('dashboard.index'))
        except Exception as e:
            db.session.rollback()
            flash('Error al agregar el egreso', 'danger')
            print(f"Error al agregar el egreso: {e}")
    else:
        print("Validación fallida:", form.errors)

    return render_template('add_transaction.html', form=form, tipo_transaccion='Egreso')
