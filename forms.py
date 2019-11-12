from flask_wtf import Form

from wtforms import StringField, SubmitField, IntegerField, HiddenField
from wtforms.validators import Required


class rubikForm(Form):
	n = IntegerField('Provide n for nXnXn Rubiks\'s Cube ', validators=[Required()])
	submit = SubmitField('Know Rubik\' Cube Details')


class rubikFormM(Form):
	m = HiddenField('Provide n-2 for nXnXn Rubiks\'s Cube ', validators=[Required()])
	submit = SubmitField('Remove All Cubelets Making Up The Faces')