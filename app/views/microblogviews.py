from app import app
from flask import render_template
from flask import flash
from flask import redirect
from app.views.forms import LoginForm

@app.route('/')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    template_naeme = 'index.html'
    return render_template(template_naeme, title='Home', user=user)

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
def posts():
    # fake user
    user = {'nickname': 'Miguel'}

    # fake array of posts
    posts = [{'author': {'nickname': 'John'}, 'body': 'Beautiful day in Portland!'},
             {'author': {'nickname': 'Susan'}, 'body': 'The Avengers movie was so cool!'}]

    template_naeme = 'posts.html'
    return render_template(template_naeme, title='Posts', posts=posts, user=user)

@app.route('/login')
def login():
    form = LoginForm()
    template_naeme = 'login.html'
    return render_template(template_naeme, title='Sign In', form=form)

@app.route('/dologin', methods=['GET', 'POST'])
def dologin():
    form = LoginForm()
    if form.validate_on_submit():
        flash('username="' + form.username.data + '", password=' + str(form.password.data))
        return redirect('/')
    else:
        template_naeme = 'login.html'
        return render_template(template_naeme, title='Sign In', form=form)
