from app import app
from flask import render_template
from flask import flash
from flask import redirect
from flask_login import login_required, current_user

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

