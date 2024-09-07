from flask import Blueprint, render_template
from models import Ingreso, Egreso
from flask_login import login_required, current_user
from extensions import db


dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
@login_required
def index():
    # Filtrar ingresos y egresos por el usuario actual
    ingresos = sum(i.importe for i in Ingreso.query.filter_by(legajousuario=current_user.legajo).all())
    egresos = sum(e.importe for e in Egreso.query.filter_by(legajousuario=current_user.legajo).all())
    
    # Filtrar datos por categoría para el usuario actual
    ingresos_por_categoria = {}
    for ingreso in Ingreso.query.filter_by(legajousuario=current_user.legajo).all():
        categoria = ingreso.categoria.nombre
        if categoria in ingresos_por_categoria:
            ingresos_por_categoria[categoria] += ingreso.importe
        else:
            ingresos_por_categoria[categoria] = ingreso.importe
    
    egresos_por_categoria = {}
    for egreso in Egreso.query.filter_by(legajousuario=current_user.legajo).all():
        categoria = egreso.categoria.nombre
        if categoria in egresos_por_categoria:
            egresos_por_categoria[categoria] += egreso.importe
        else:
            egresos_por_categoria[categoria] = egreso.importe
    
    return render_template(
        'dashboard.html',
        ingresos=ingresos,
        egresos=egresos,
        ingresos_por_categoria=ingresos_por_categoria,
        egresos_por_categoria=egresos_por_categoria
    )