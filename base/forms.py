from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField

class CodeCheck(FlaskForm):
    language = SelectField('language', choices=[('python'), ('c++'), ('c')])
    code = TextAreaField('code')
    submit = SubmitField('Submit')
