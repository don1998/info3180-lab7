from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextAreaField
from wtforms.validators import DataRequired, InputRequired



class UploadForm(FlaskForm):
    description = TextAreaField('Description',validators=[InputRequired()])
    photo = FileField(validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])