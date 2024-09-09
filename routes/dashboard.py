from flask import Blueprint, render_template, request
from models import Ingreso, Egreso
from extensions import db
from flask_login import login_required, current_user
from sqlalchemy import func

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
@login_required
def index():
    # Obtener la fecha seleccionada del formulario (si existe)
    fecha_seleccionada = request.args.get('fecha')

    # Inicializar variables para ingresos y egresos filtrados por día
    ingresos_dia = 0
    egresos_dia = 0

    # Obtener los ingresos y egresos totales generales
    ingresos_totales = db.session.query(func.sum(Ingreso.importe)).filter_by(legajousuario=current_user.legajo).scalar() or 0
    egresos_totales = db.session.query(func.sum(Egreso.importe)).filter_by(legajousuario=current_user.legajo).scalar() or 0

    # Filtrar ingresos y egresos por día si la fecha está seleccionada
    if fecha_seleccionada:
        ingresos_dia = db.session.query(func.sum(Ingreso.importe)).filter_by(legajousuario=current_user.legajo).filter(func.date(Ingreso.fecha) == fecha_seleccionada).scalar() or 0
        egresos_dia = db.session.query(func.sum(Egreso.importe)).filter_by(legajousuario=current_user.legajo).filter(func.date(Egreso.fecha) == fecha_seleccionada).scalar() or 0

    # Datos por categoría para los gráficos (de todos los ingresos/egresos, sin filtrar por fecha)
    ingresos = db.session.query(Ingreso).filter_by(legajousuario=current_user.legajo).all()
    egresos = db.session.query(Egreso).filter_by(legajousuario=current_user.legajo).all()

    ingresos_por_categoria = {}
    for ingreso in ingresos:
        categoria = ingreso.categoria.nombre
        if categoria in ingresos_por_categoria:
            ingresos_por_categoria[categoria] += ingreso.importe
        else:
            ingresos_por_categoria[categoria] = ingreso.importe

    egresos_por_categoria = {}
    for egreso in egresos:
        categoria = egreso.categoria.nombre
        if categoria in egresos_por_categoria:
            egresos_por_categoria[categoria] += egreso.importe
        else:
            egresos_por_categoria[categoria] = egreso.importe

    return render_template(
        'dashboard.html',
        ingresos_totales=ingresos_totales,
        egresos_totales=egresos_totales,
        ingresos_dia=ingresos_dia,
        egresos_dia=egresos_dia,
        ingresos_por_categoria=ingresos_por_categoria,
        egresos_por_categoria=egresos_por_categoria,
        fecha=fecha_seleccionada
    )
