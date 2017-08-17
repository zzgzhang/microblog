from flask_wtf import Form
from wtforms import StringField, PasswordField, FileField, TextAreaField
from wtforms.validators import DataRequired, Length


class LoginForm(Form):
    username = StringField(label='Username', validators=[DataRequired(message='username is required.')])
    password = PasswordField(label='Password', validators=[DataRequired(message='password is required.')])


class EditForm(Form):
    nickname = StringField(label='Nickname', validators=[DataRequired(message='nickname is required.')])
    description = TextAreaField(label='About Me', validators=[Length(min=0, max=140)])
    image = FileField(label='Image')


class NewUserForm(Form):
    username = StringField(label='Username', validators=[DataRequired(message='username is required.')])
    password = PasswordField(label='Password', validators=[DataRequired(message='password is required.')])
    nickname = StringField(label='Nickname', validators=[DataRequired(message='nickname is required.')])
    description = TextAreaField(label='About Me', validators=[Length(min=0, max=140)])


class PostForm(Form):
    post = TextAreaField(label='Post', validators=[
        Length(min=20, max=500, message='You should input no less than 20 words, no more than 500 words.')])
