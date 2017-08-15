from flask_wtf import Form
from wtforms import StringField, PasswordField, FileField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(Form):
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])

class EditForm(Form):
    nickname = StringField(label='Nickname', validators=[DataRequired()])
    description = TextAreaField(label='About Me', validators=[Length(min=0, max=140)])
    image = FileField(label='Image')