#from flask_wtf import Form
from flask_wtf import FlaskForm as BaseForm
from wtforms import StringField, SubmitField, IntegerField, HiddenField
from wtforms.validators import Required

#class rubikForm(Form):
class rubikForm(BaseForm):
	n = IntegerField('Provide n for nXnXn ', validators=[Required()])
	submit = SubmitField('Rubik\' Cube Details')

#class rubikFormM(Form):
class rubikFormM(BaseForm):
	m = HiddenField('Provide n-2 for nXnXn Rubiks\'s Cube ', validators=[Required()])
	submit = SubmitField('Remove All Cubelets Making Up The Faces')
