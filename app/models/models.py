import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from app.models import engine
from sqlalchemy.orm import relationship

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(20), nullable=False)
    password = sa.Column(sa.String(20), nullable=False)
    nickname = sa.Column(sa.String(64), nullable=False)
    email = sa.Column(sa.String(120), nullable=False)
    description = sa.Column(sa.String(500), nullable=False, server_default=' ', default=' ')
    # server_default在数据库中设置字段的默认值，default是设置sqlalchemy提交是的默认值
    imgpath = sa.Column(sa.String(30), nullable=False, server_default='default.jpg', default='default.jpg')
    last_seen = sa.Column(sa.DateTime())

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return 'username:%s, password:%s' % (self.username, self.password)

    def get_imgpath(self):
        img_path = '../static/resources/' + self.imgpath
        return img_path

class Posts(Base):
    __tablename__ = 'posts'

    id = sa.Column(sa.Integer, primary_key=True)
    body = sa.Column(sa.String(500), nullable=True)
    timestamp = sa.Column(sa.Time(), nullable=True)
    user_id = sa.Column(sa.Integer(), sa.ForeignKey('users.id'))
    author = relationship('Users')

    def __repr__(self):
        return '%s' % self.body

if __name__ == "__main__":
    Base.metadata.create_all(engine)
