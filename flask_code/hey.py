from flask import Flask

app = Flask(__name__)  # 实例化app实例


# app=Flask(__name__,static_folder='static',static_url_path='/static')#可以改静态文件夹的名字和路径
# app=Flask(__name__,template_folder='templates',static_url_path='/templates')#可以改模板文件夹的名字和路径

@app.route('/')  # 路由
def index():  # 视图
    return 'hello world'  # 返回值


# -----------------------------最好路由和函数名相同，且视图名不可重复
@app.route('/hello')
def hello():
    return 'hello'


# -------------------------------------转化器语法
# 转换器语法：默认类型为string，路由有的参数，视图函数中必须写,改类型用 类型：
@app.route('/hello/<name>/<int:age>/<path:url>')
def hello1(name, age, url):
    print('我的网址：', url)
    return '我的名字叫%s，今年%s岁' % (name, age)


# --------------------------------------获取请求----------------------
# -----默认支持get请求,获取get请求参数,request.args.get（'key'）
from flask import request


@app.route('/reqdemo_get/')
def reqdemo_get():
    name = request.args.get('name')
    print(name)
    return 'reqdemo_get'


# ----------------------------
# flask默认不支持post请求,获取使用request.form.get（'key'）
@app.route('/reqdemo_post/', methods=['post','get'])
def reqdemo_post():
    name = request.form.get('name')
    print(name)
    return 'post请求获得的name:%s'%name


# -------------------------------返回一个html页面----
from flask import redirect, render_template


@app.route('/getindex/')
def getindex():
    # -----传递数据方法一
    # return render_template('getindex.html',name='张三')

    # -----传递数据方法二
    # name='张三'
    # return render_template('getindex.html',name=name)

    # -----传递数据方法三
    name = '张三'
    mydict = {'name': 'Barry Alen', 'age': 24}
    return render_template('getindex.html', **locals())


# --------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)  # 项目启动，默认5000端口，可以自己修改
    # 开启debug模式：1.显示错误内容，修改代码之后自动重启
    # app.run(host="127.0.0.1", port=8000, debug=True, )
