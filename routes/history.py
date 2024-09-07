from flask import Blueprint, render_template, redirect, url_for, flash
from extensions import db
from models import Ingreso, Egreso
from flask_login import login_required,current_user

history_bp = Blueprint('history', __name__)

@history_bp.route('/history', methods=['GET'])
@login_required
def show_history():
    ingresos = Ingreso.query.filter_by(legajousuario=current_user.legajo).all()
    egresos = Egreso.query.filter_by(legajousuario=current_user.legajo).all()
    return render_template('history.html', ingresos=ingresos, egresos=egresos)

@history_bp.route('/delete_ingreso/<int:id>', methods=['POST'])
def delete_ingreso(id):
    ingreso = Ingreso.query.get_or_404(id)
    if ingreso.legajousuario != current_user.legajo:
        flash("No puedes eliminar esta transacción", 'danger')
        return redirect(url_for('history.show_history'))
    
    db.session.delete(ingreso)
    db.session.commit()
    flash('Ingreso eliminado correctamente', 'success')
    return redirect(url_for('history.show_history'))

@history_bp.route('/delete_egreso/<int:id>', methods=['POST'])
def delete_egreso(id):
    egreso = Egreso.query.get_or_404(id)
    if egreso.legajousuario != current_user.legajo:
        flash("No puedes eliminar esta transacción", 'danger')
        return redirect(url_for('history.show_history'))
    
    db.session.delete(egreso)
    db.session.commit()
    flash('Egreso eliminado correctamente', 'success')
    return redirect(url_for('history.show_history'))
