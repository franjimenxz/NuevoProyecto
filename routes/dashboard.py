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

    # Obtener los ingresos y egresos totales para el usuario actual
    ingresos_totales = db.session.query(func.sum(Ingreso.importe)).filter_by(legajousuario=current_user.legajo).scalar() or 0
    egresos_totales = db.session.query(func.sum(Egreso.importe)).filter_by(legajousuario=current_user.legajo).scalar() or 0

    # Filtrar ingresos y egresos por día
    if fecha_seleccionada:
        ingresos = db.session.query(Ingreso).filter_by(legajousuario=current_user.legajo).filter(func.date(Ingreso.fecha) == fecha_seleccionada).all()
        egresos = db.session.query(Egreso).filter_by(legajousuario=current_user.legajo).filter(func.date(Egreso.fecha) == fecha_seleccionada).all()
    else:
        ingresos = db.session.query(Ingreso).filter_by(legajousuario=current_user.legajo).all()
        egresos = db.session.query(Egreso).filter_by(legajousuario=current_user.legajo).all()

    # Agrupar ingresos y egresos por día
    ingresos_por_dia = db.session.query(func.date(Ingreso.fecha), func.sum(Ingreso.importe)).filter_by(legajousuario=current_user.legajo).group_by(func.date(Ingreso.fecha)).all()
    egresos_por_dia = db.session.query(func.date(Egreso.fecha), func.sum(Egreso.importe)).filter_by(legajousuario=current_user.legajo).group_by(func.date(Egreso.fecha)).all()

    # Datos por categoría para los gráficos
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
        ingresos=ingresos_totales,
        egresos=egresos_totales,
        ingresos_por_categoria=ingresos_por_categoria,
        egresos_por_categoria=egresos_por_categoria,
        ingresos_por_dia=ingresos_por_dia,
        egresos_por_dia=egresos_por_dia,
        fecha=fecha_seleccionada
    )
