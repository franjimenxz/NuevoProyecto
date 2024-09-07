from flask import Blueprint, render_template, redirect, url_for, flash
from forms import TransactionForm
from models import Ingreso, Egreso, Categoria
from extensions import db
from flask_login import current_user

transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route('/add_income', methods=['GET', 'POST'])
def add_income():
    form = TransactionForm()
    form.idcategoria.choices = [(c.id, c.nombre) for c in Categoria.query.filter_by(tipo='Ingreso').all()]
    
    if form.validate_on_submit():
        nuevo_ingreso = Ingreso(
            descripcion=form.descripcion.data,
            importe=form.importe.data,
            idcategoria=form.idcategoria.data,
            legajousuario=current_user.legajo  # Aquí añades el legajousuario del usuario autenticado
        )
        db.session.add(nuevo_ingreso)
        db.session.commit()
        flash('Ingreso agregado correctamente', 'success')
        return redirect(url_for('dashboard.index'))
    
    return render_template('add_transaction.html', form=form)

@transactions_bp.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    form = TransactionForm()
    form.idcategoria.choices = [(c.id, c.nombre) for c in Categoria.query.filter_by(tipo='Egreso').all()]
    
    if form.validate_on_submit():
        nuevo_egreso = Egreso(
            descripcion=form.descripcion.data,
            importe=form.importe.data,
            idcategoria=form.idcategoria.data,
            legajousuario=current_user.legajo  # Aquí añades el legajousuario del usuario autenticado
        )
        db.session.add(nuevo_egreso)
        db.session.commit()
        flash('Egreso agregado correctamente', 'success')
        return redirect(url_for('dashboard.index'))
    
    return render_template('add_transaction.html', form=form)
