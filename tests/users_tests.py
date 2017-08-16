import unittest
from app.controller.usercontroller import UserController
from app.models import session
from app.models.models import Users
from datetime import datetime

class UsersTestCase(unittest.TestCase):
    def test_follow(self):
        u1 = Users()
        u1.username = 'json'
        u1.password = '123456'
        u1.nickname = 'Json'
        u1.description = 'This is Json'
        u1.email = 'Json@json.com'
        u1.imgpath = 'default.jpg'
        u1.last_seen = datetime.utcnow()
        u2 = Users()
        u2.username = 'kathy'
        u2.password = '123456'
        u2.nickname = 'Kathy'
        u2.description = 'This is Kathy'
        u2.email = 'Kathy@json.com'
        u2.imgpath = 'default.jpg'
        u2.last_seen = datetime.utcnow()
        session.add(u1)
        session.add(u2)
        session.commit()

        self.assertEqual(u1.unfollow(u2), None)

        u = u1.follow(u2)
        session.add(u)
        session.commit()
        self.assertEqual(u1.is_following(u2), True)
        self.assertEqual(u1.followed.count(), 1)
        self.assertEqual(u2.followers.count(), 1)




    def test_get_imgpath(self):
        userController = UserController()
        user = userController.query_byname('test2')
        img_path = user.get_imgpath()
        self.assertEqual(img_path, '../static/resources/default.jpg')


if __name__ == '__main__':
    unittest.main()
