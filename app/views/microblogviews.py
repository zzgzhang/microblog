from app import app
from flask import render_template
from flask import request
from flask import session

@app.route('/')
def hello_world():
    return 'Hello World!'

