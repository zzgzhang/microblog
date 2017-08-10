from flask import Flask
from app import config
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(config)
# 注册Login管理
lm = LoginManager()
lm.session_protection = 'strong'
lm.login_view = 'auth.login'
lm.init_app(app)

from app.views import microblogviews
from app.views import authviews
# 注册Blueprint模块
app.register_blueprint(authviews.auth, url_prefix='/auth')