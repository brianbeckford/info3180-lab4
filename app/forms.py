from flask import url_for, redirect, render_template
from flask_wtf import Form
from flask_wtf.file import FileField,FileRequired,FileAllowed
from werkzeug import secure_filename

 
class UploadForm(Form):
    photo = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])


    
    