#!flask/bin/python
import os

pybabel = '/Users/wzy/flask/bin/pybabel'
os.chdir('/Users/wzy/Documents/PycharmProjects/microblog/app')
os.system(pybabel + ' extract -F babel.cfg -k lazy_gettext -o messages.pot .')
os.system(pybabel + ' init -i messages.pot -d translations -l zh')
#os.unlink('messages.pot')
