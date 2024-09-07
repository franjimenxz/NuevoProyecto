from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, SelectField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length

class RegisterForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(), Length(min=3, max=25)])
    nombre = StringField('Nombre', validators=[DataRequired()])
    dni = StringField('DNI', validators=[DataRequired()])
    contrasena = PasswordField('Contraseña', validators=[DataRequired()])
    confirmar_contrasena = PasswordField('Confirmar Contraseña', validators=[DataRequired(), EqualTo('contrasena')])
    submit = SubmitField('Registrar')

class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired()])
    contrasena = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class TransactionForm(FlaskForm):
    descripcion = TextAreaField('Descripción', validators=[DataRequired()])
    importe = FloatField('Importe', validators=[DataRequired()])
    idcategoria = SelectField('Categoría', choices=[], validators=[DataRequired()])
    
    # Campo opcional para método de pago
    idmetodopago = SelectField('Método de Pago', choices=[], validators=[], render_kw={"optional": True})  # Sin validador requerido
    
    submit = SubmitField('Agregar')