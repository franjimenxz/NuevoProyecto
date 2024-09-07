from flask import Blueprint, render_template, redirect, url_for, flash
from forms import TransactionForm
from models import Ingreso, Egreso, Categoria, MetodoPago
from extensions import db
from flask_login import current_user

transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route('/add_income', methods=['GET', 'POST'])
def add_income():
    form = TransactionForm()
    
    # Solo cargar categorías de ingreso
    form.idcategoria.choices = [(c.id, c.nombre) for c in Categoria.query.filter_by(tipo='Ingreso').all()]
    
    # NO cargar el campo de método de pago
    form.idmetodopago = None

    if form.validate_on_submit():
        nuevo_ingreso = Ingreso(
            descripcion=form.descripcion.data,
            importe=form.importe.data,
            idcategoria=form.idcategoria.data,
            legajousuario=current_user.id
        )
        db.session.add(nuevo_ingreso)
        db.session.commit()
        flash('Ingreso agregado correctamente', 'success')
        return redirect(url_for('dashboard.index'))

    return render_template('add_transaction.html', form=form, tipo_transaccion='Ingreso')



@transactions_bp.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    form = TransactionForm()

    # Cargar categorías de egreso
    form.idcategoria.choices = [(c.id, c.nombre) for c in Categoria.query.filter_by(tipo='Egreso').all()]

    # Cargar los métodos de pago
    form.idmetodopago.choices = [(m.id, m.nombre) for m in MetodoPago.query.all()]

    if form.validate_on_submit():
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
        return redirect(url_for('dashboard.index'))

    return render_template('add_transaction.html', form=form, tipo_transaccion='Egreso')
