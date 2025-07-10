from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class CadastroForm():
    user = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    cpf = IntegerField('Cpf', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')