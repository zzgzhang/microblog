import os
basedir = os.path.abspath(os.path.dirname(__file__))

# 数据库链接设置
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'microblog.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
# SECRET_KEY设置当CSRF启用时有效，这将生成一个加密的token供表单验证使用，你要确保这个KEY足够复杂不会被简单推测。
SECRET_KEY = 'you-will-never-guess'