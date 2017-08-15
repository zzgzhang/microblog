from app import app
from flask import render_template
from flask import flash
from flask import redirect
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
from app.controller.usercontroller import UserController
from flask import url_for
from datetime import datetime
from app.views.forms import EditForm, NewUserForm
from os.path import join
from os import remove
from app.models import session
from flask_login import login_user

@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    session.rollback()
    return render_template('500.html'), 500


@app.route('/')
@login_required
def index():
    '''
    user = current_user
    template_naeme = 'index.html'
    return render_template(template_naeme, title='Home', user=user)
    '''
    return redirect('/posts')

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/html')
def html():
    user = {'nickname': 'Miguel'}  # fake user
    return '''
    <html>
      <head>
        <title>Home Page</title>
      </head>
      <body>
        <h1>Hello, ''' + user['nickname'] + '''</h1>
      </body>
    </html>
    '''

@app.route('/posts')
@login_required
def posts():
    # fake user
    user = current_user

    # fake array of posts
    posts = [{'author': {'nickname': 'John'}, 'body': 'Beautiful day in Portland!'},
             {'author': {'nickname': 'Susan'}, 'body': 'The Avengers movie was so cool!'}]

    template_naeme = 'posts.html'
    return render_template(template_naeme, title='Posts', posts=posts, user=user)

@app.route('/user/<username>')
@login_required
def user(username):
    userController = UserController()
    user = userController.query_byname(username=username)

    if user == None:
        flash('User ' + username + ' not found.')
        return redirect('/')

    posts = [{ 'author': user, 'body': 'Test post #1' }, { 'author': user, 'body': 'Test post #2' }]
    return render_template('user.html',
        user = user,
        posts = posts)

@app.before_request
def before_request():

    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        userController = UserController()
        userController.update(current_user)

@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditForm()
    if form.validate_on_submit():
        current_user.nickname = form.nickname.data
        current_user.description = form.description.data
        file = form.image.data

        if file:
            # 保存上传的文件
            fileName = str(current_user.username) + secure_filename(file.filename)
            path = join(app.config['UPLOAD_FOLDER'], fileName)

            if current_user.imgpath != 'default.jpg':
                try:
                    remove(join(app.config['UPLOAD_FOLDER'], current_user.imgpath))
                except:
                    print('There is no file to be deleted!')

            file.save(path)
            current_user.imgpath = fileName

            flash('Your changes have been saved.')

        return redirect(url_for('edit'))
    else:
        form.nickname.data = current_user.nickname
        form.description.data = current_user.description
    return render_template('edit.html', title='Edit User', form=form)

@app.route('/newuser', methods=['GET', 'POST'])
def newuser():
    form = NewUserForm()
    if form.validate_on_submit():
        username = form.username.data
        userController = UserController()
        user = userController.query_byname(username)
        if user:
            flash('The username is signned up, please use another username!')
            render_template('newuser.html', title='Sign Up', form=form)
        else:
            password = form.password.data
            nickname = form.nickname.data
            description = form.description.data
            user = userController.add(username=username, password=password, nickname=nickname, description=description)
            login_user(user)
            return redirect(url_for('user', username=username))

    return render_template('newuser.html', title='Sign Up', form=form)



