from app.models.models import Users, Posts
from app.models import session

# 增加数据
'''user = Users()
user.username = 'wzy'
user.password = 'zaq12wsx'
user.nickname = 'Kevin'
user.email = 'weizy@cn.ibm.com'
user.description = 'This is a test user'
session.add(user)
user = Users()
user.username = 'zzz'
user.password = 'zaq12wsx'
user.nickname = 'Kevin'
user.email = 'zzz@cn.ibm.com'
user.description = 'This is a test user'
session.commit()
session.close()

# 查询Users中的全部数据，返回的是一个List对象
users = session.query(Users).all()
print(users)

# 查询单个数据，get的数据是从1开始
user = session.query(Users).get(1)
user.follow(user)
session.add(user)
session.commit()
print(user)

# 更新数据
user.password = 'xsw23edc'
session.add(user)
session.commit()
session.close()

# 查询Users中username=wzy的全部记录，返回的是一个List对象
users_f = session.query(Users).filter_by(username='wzy').all()
print((users_f))

# 删除数据
user = session.query(Users).get(2)
print(user)
session.delete(user)
session.commit()
session.close()
users = session.query(Users).all()
print(users)'''

# 删除全部Posts
posts = session.query(Posts).all()
for post in posts:
    session.delete(post)
    session.commit()
    session.close()


