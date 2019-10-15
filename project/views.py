import timetest, hashlib, time, os, functools
from main import *
from models import *
from flask import request, render_template, redirect, session
from settings import *


# --------------------------密码加密
def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result


# ---------------------------注册页面
@app.route('/register/', methods=['post', 'get'])
def register():
    error_msg = ''
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        password1 = request.form.get('password1')
        user = User.query.filter_by(email=email).first()
        if email and password and password1:
            if user:
                error_msg = '账户已存在'
            else:
                if password != password1:
                    error_msg = '两次密码不一致'
                else:
                    user = User(email=email, password=setPassword(password))
                    db.session.add(user)
                    db.session.commit()
                    error_msg = '注册成功，3秒后跳转登录页。。。'

        else:
            error_msg = '请输入完信息后再提交'
    return render_template('register.html', **locals())


# ----------------------------------登录页面
@app.route('/', methods=['post', 'get'])
def login():
    error_msg = ''
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        if email and password:
            user = User.query.filter_by(email=email).first()
            id = user.id
            print(id)
            if user:
                if user.password == setPassword(password):
                    error_msg = '登录成功'
                    response = redirect('/index/')
                    response.set_cookie('email', email)  # 设置cookie
                    response.set_cookie('user_id', str(id))  # 设置cookie
                    session['email'] = email  # 设置session
                    return response
                else:
                    error_msg = '密码错误'
            else:
                error_msg = '账户不存在'
        else:
            error_msg = '请输入完整后再提交'
    return render_template('login.html', **locals())


# --------------------------------登录装饰器
def LoginVaild(func):
    @functools.wraps(func)  # 保留原理的函数名字
    def inner(*args, **kwargs):
        cookie_email = request.cookies.get('email')
        session_email = session.get('email')
        if cookie_email and session_email and cookie_email == session_email:
            user = User.query.filter_by(email=cookie_email).first()
            if user:
                return func(*args, **kwargs)
            else:
                return redirect('/')
        else:
            return redirect('/')

    return inner


# ----------------------------------退出
@app.route('/logout/', methods=['get', 'post'])
def logout():
    rep = redirect('/')
    rep.delete_cookie('email')
    session.pop('email')
    return rep


# ------------------------------------首页
@app.route('/index/')
@LoginVaild
def index():
    print(request.cookies.get('email'), session.get('email'))
    return render_template('index.html')


# ---------------------------------个人中心页
@app.route('/userinfo/')
@LoginVaild
def userinfo():
    result = timetest.MyDate()
    time = result.get_date()  # 将日历展示
    email = request.cookies.get('email')
    user = User.query.filter_by(email=email).first()
    print('../static/img/' + user.photo)
    return render_template('userinfo.html', **locals())


# ------------------------------------更新个人中心
@app.route('/update_userinfo/', methods=['post', 'get'])
@LoginVaild
def update_userinfo():
    email = request.cookies.get('email')
    user = User.query.filter_by(email=email).first()
    if request.method == 'POST':
        # 先存图片
        photo = request.files.get('photo')
        file_name = photo.filename
        photo_path = os.path.join('img', file_name)  # img/图片
        path = os.path.join(STATIC_PATH, photo_path)
        photo.save(path)
        user.photo = photo_path
        user.age = request.form.get('age')
        user.sex = request.form.get('sex')
        user.name = request.form.get('name')
        user.identity = request.form.get('identity')
        user.subject = request.form.get('subject')
        user.level = request.form.get('level')
        user.merge()

    return render_template('update_userinfo.html', **locals())


# -------------------------请假条
@app.route('/leave_list/', methods=['get', 'post'])
def leave_list():
    if request.method == "POST":
        user_id = request.cookies.get("user_id")
        data = request.form
        start_time = data.get("start")
        end_time = data.get("end")
        print(start_time,type(start_time))
        leave = Leave_User()
        leave.request_id = int(user_id)  ## 请假人id
        leave.request_name = data.get("username")  ## 请假人姓名
        leave.request_type = data.get("type")  ### 假期类型
        leave.request_start = start_time  ## 请假的开始时间
        leave.request_end = end_time  ## 请假的结束时间
        leave.request_description = data.get("dec")  ## 请假描述
        leave.request_phone = data.get("phone")  ###联系人手机号
        leave.request_day = data.get("day")  ###联系人手机号
        leave.request_status = 0  ## 请假状态
        db.session.add(leave)
        db.session.commit()
        return redirect("/leave_all_list/")
    return render_template('leave_list.html', **locals())


# ---------------------------所有请假条
@app.route('/leave_all_list/')
def leave_all_list():
    user_id = request.cookies.get('user_id')
    leave = Leave_User.query.filter_by(request_id=user_id).all()
    print(leave)
    return render_template('leave_all_list.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)
