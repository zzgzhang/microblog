import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from app.models import engine
from sqlalchemy.orm import relationship, backref
from app.models import session

Base = declarative_base()

followers = sa.Table('followers', Base.metadata,
                     sa.Column('follower_id', sa.Integer, sa.ForeignKey('users.id')),
                     sa.Column('followed_id', sa.Integer, sa.ForeignKey('users.id'))
                     )


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

    followed = relationship('Users',
                            secondary=followers,
                            primaryjoin=(followers.c.follower_id == id),
                            secondaryjoin=(followers.c.followed_id == id),
                            backref=backref('followers', lazy='dynamic'),
                            lazy='dynamic')


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

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)
            return self

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)
            return self

    def is_following(self, user):
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

    def followed_posts(self):
        return session.query(Posts).join(followers, (followers.c.followed_id == Posts.user_id)).filter(
            followers.c.follower_id == self.id).order_by(Posts.timestamp.desc())


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
