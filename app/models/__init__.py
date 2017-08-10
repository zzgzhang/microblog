import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
engine = sa.create_engine("sqlite:////Users/wzy/Documents/PycharmProjects/microblog/app/microblog.db")
DBSession = sessionmaker(engine)
