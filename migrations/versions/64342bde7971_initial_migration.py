"""Initial migration

Revision ID: 64342bde7971
Revises: 
Create Date: 2024-09-06 22:19:52.519525

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '64342bde7971'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('metodopago')
    op.drop_table('usuarios')
    op.drop_table('ingresos')
    op.drop_table('categorias')
    op.drop_table('egresos')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('egresos',
    sa.Column('codigo', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('idcategoria', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('legajousuario', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('descripcion', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('fecha', sa.DATE(), server_default=sa.text('CURRENT_DATE'), autoincrement=False, nullable=False),
    sa.Column('hora', postgresql.TIME(), server_default=sa.text('CURRENT_TIME'), autoincrement=False, nullable=False),
    sa.Column('destinatario', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('importe', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('impuestos', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('idmetodopago', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['idcategoria'], ['categorias.id'], name='fk_egreso_categoria'),
    sa.ForeignKeyConstraint(['idmetodopago'], ['metodopago.id'], name='fk_egreso_metodopago'),
    sa.ForeignKeyConstraint(['legajousuario'], ['usuarios.legajo'], name='fk_egreso_usuario'),
    sa.PrimaryKeyConstraint('codigo', name='egresos_pkey')
    )
    op.create_table('categorias',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('categorias_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('tipo', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='categorias_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('ingresos',
    sa.Column('codigo', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('idcategoria', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('legajousuario', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('descripcion', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('fecha', sa.DATE(), server_default=sa.text('CURRENT_DATE'), autoincrement=False, nullable=False),
    sa.Column('hora', postgresql.TIME(), server_default=sa.text('CURRENT_TIME'), autoincrement=False, nullable=False),
    sa.Column('importe', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['idcategoria'], ['categorias.id'], name='fk_ingreso_categoria'),
    sa.ForeignKeyConstraint(['legajousuario'], ['usuarios.legajo'], name='fk_ingreso_usuario'),
    sa.PrimaryKeyConstraint('codigo', name='ingresos_pkey')
    )
    op.create_table('usuarios',
    sa.Column('legajo', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('dni', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('usuario', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('contrasena', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('nrocuenta', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('tipo_usuario', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('legajo', name='usuarios_pkey'),
    sa.UniqueConstraint('dni', name='usuarios_dni_key'),
    sa.UniqueConstraint('usuario', name='usuarios_usuario_key')
    )
    op.create_table('metodopago',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='metodopago_pkey')
    )
    # ### end Alembic commands ###
