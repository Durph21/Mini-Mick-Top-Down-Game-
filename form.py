from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, RadioField, SelectField, PasswordField
from wtforms.validators import InputRequired, EqualTo

class ScoreForm(FlaskForm):
    name = StringField("Team Name: ", validators=[InputRequired()])
    submit = SubmitField("Submit")