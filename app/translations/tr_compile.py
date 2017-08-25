#!flask/bin/python
import os

pybabel = '/Users/wzy/flask/bin/pybabel'
os.chdir('/Users/wzy/Documents/PycharmProjects/microblog/app')
os.system(pybabel + ' compile -d translations')
