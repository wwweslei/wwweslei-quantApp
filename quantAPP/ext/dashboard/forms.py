from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, FloatField, SelectField, SubmitField, DateTimeField
from wtforms.validators import InputRequired, ValidationError


def validate_ticket(form, field):
    if len(field.data) > 50:
        raise ValidationError('O ticket não é valido')

class WalletForm(FlaskForm):
    ticket = StringField("Ticket", validators=[InputRequired(), validate_ticket])
    kind = SelectField(
        "Tipo", choices=["Compra", "Venda"], validators=[InputRequired()])
    date = DateTimeField("Data", validators=[InputRequired()])
    amount = IntegerField("Quantidade", validators=[InputRequired()])
    price = FloatField("Preço", validators=[InputRequired()])
    commission = FloatField("Comissão", validators=[InputRequired()])
    submit = SubmitField('Adicionar')
