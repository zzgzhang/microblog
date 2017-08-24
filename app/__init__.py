from flask import Flask
from app import config
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler
from logging.handlers import RotatingFileHandler
from flask_mail import Mail
from app.utils.momentjs import Momentjs
from flask_babel import Babel, lazy_gettext

app = Flask(__name__)
app.config.from_object(config)
# 注册Login管理
lm = LoginManager()
lm.login_message = lazy_gettext('Please log in to access this page.')
lm.session_protection = 'strong'
lm.login_view = 'auth.login'
lm.init_app(app)
mail = Mail(app)
babel = Babel(app)

# 使用MomentJs
app.jinja_env.globals['momentjs'] = Momentjs

# 路由设定
from app.views import microblogviews
from app.views import authviews
# 注册Blueprint模块
app.register_blueprint(authviews.auth, url_prefix='/auth')

# 发送邮件
if not app.debug:
    credentials = None
    if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
        credentials = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
    mail_handler = SMTPHandler((app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                               'no-reply@' + app.config['MAIL_SERVER'], app.config['ADMINS'], 'microblog failure',
                               credentials)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

# 记录log
if not app.debug:
    file_handler = RotatingFileHandler(app.config['LOG_FILE'], 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('microblog startup')

