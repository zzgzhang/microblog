import unittest
from app.controller.usercontroller import UserController

class UsersTestCase(unittest.TestCase):
    def test_get_imgpath(self):
        userController = UserController()
        user = userController.query_byname('test2')
        img_path = user.get_imgpath()
        self.assertEqual(img_path, '../static/resources/default.jpg')


if __name__ == '__main__':
    unittest.main()
