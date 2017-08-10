from flask import Blueprint, flash, redirect, render_template, g
from flask_login import login_required, login_user, logout_user, current_user
from app import lm
from app.models.models import Users
from app.views.forms import LoginForm
from app.controller.usercontroller import UserController

@lm.user_loader
def user_load(user_id):
    user_controller = UserController()
    user = user_controller.query_byId(user_id=int(user_id))
    return user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # 如果已经Login，重定向到首页
    if current_user.is_authenticated:
        return redirect('/')

    form = LoginForm()
    if form.validate_on_submit():
        #flash('username="' + form.username.data + '", password=' + str(form.password.data))
        username = form.username.data
        password = form.password.data
        user_controller = UserController()
        user = user_controller.query(username=username, password=password)
        # 是否是注册用户
        if user:
            login_user(user)
            return redirect('/')
        else:
            flash('username or password is worry')
            return redirect('/auth/login')
    else:
        template_naeme = 'login.html'
        return render_template(template_naeme, title='Sign In', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('user is logout')
    return redirect('/auth/login')
