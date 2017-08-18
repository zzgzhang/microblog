from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, TextAreaField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(message='username is required.')])
    password = PasswordField(label='Password', validators=[DataRequired(message='password is required.')])


class EditForm(FlaskForm):
    nickname = StringField(label='Nickname', validators=[DataRequired(message='nickname is required.')])
    description = TextAreaField(label='About Me', validators=[Length(min=0, max=140)])
    image = FileField(label='Image')


class NewUserForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(message='username is required.')])
    password = PasswordField(label='Password', validators=[DataRequired(message='password is required.')])
    nickname = StringField(label='Nickname', validators=[DataRequired(message='nickname is required.')])
    description = TextAreaField(label='About Me', validators=[Length(min=0, max=140)])


class PostForm(FlaskForm):
    post = TextAreaField(label='Post', validators=[
        Length(min=20, max=500, message='You should input no less than 20 words, no more than 500 words.')])

class SearchForm(FlaskForm):
    search = StringField(label='Search', validators=[DataRequired(message='query key is required.')])
