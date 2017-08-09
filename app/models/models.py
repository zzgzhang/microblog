import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(20), nullable=False)
    password = sa.Column(sa.String(20), nullable=False)
    nickname = sa.Column(sa.String(64), nullable=False)
    email = sa.Column(sa.String(120), nullable=False)
    # 增加一个新字段description
    description = sa.Column(sa.String(200), nullable=False)

class Posts(Base):
    __tablename__ = 'posts'

    id = sa.Column(sa.Integer, primary_key=True)
    body = sa.Column(sa.String(500), nullable=True)
    timestamp = sa.Column(sa.Time(), nullable=True)
    user_id = sa.Column(sa.Integer(), nullable=True)

if __name__ == "__main__":
    engine = sa.create_engine("sqlite:////Users/wzy/Documents/PycharmProjects/microblog/app/microblog.db")
    Base.metadata.create_all(engine)
