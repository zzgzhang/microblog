from app.models.models import Users
from app.models import session

class UserController:
    def query(self, username, password):
        user = session.query(Users).filter_by(username=username, password=password).first()
        return user

    def query_byId(self, user_id):
        user = session.query(Users).filter_by(id=user_id).first()
        return user