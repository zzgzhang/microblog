from app.models.models import Users
from app.models import session

class UserController:
    def query(self, username, password):
        user = session.query(Users).filter_by(username=username, password=password).first()
        return user

    def query_byId(self, user_id):
        user = session.query(Users).filter_by(id=user_id).first()
        return user

    def query_byname(self, username):
        user = session.query(Users).filter_by(username=username).first()
        return user

    def update(self, user):
        session.add(user)
        session.commit()

    def add(self, username, password, nickname, description):
        user = Users()
        user.username = username
        user.password = password
        user.nickname = nickname
        user.description = description
        user.email = ''
        user.imgpath = 'default.jpg'
        session.add(user)
        session.commit()
        return user