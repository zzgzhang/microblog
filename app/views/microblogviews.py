from app import app
from flask import render_template

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
