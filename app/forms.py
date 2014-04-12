from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required

class SampleForm(Form):
	myform = TextField('myform')